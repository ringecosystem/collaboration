#!/usr/bin/env python3
"""Approval-gated Cloudinary -> IFTTT -> X image post publisher."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request
import uuid


ALLOWED_MIME_TYPES = {"image/jpeg", "image/png"}
REPO_ROOT = Path(__file__).resolve().parent


def fail(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upload an image to Cloudinary and post it to X through IFTTT."
    )
    text_group = parser.add_mutually_exclusive_group(required=True)
    text_group.add_argument("--text", help="Post text.")
    text_group.add_argument("--text-file", type=Path, help="UTF-8 file containing post text.")
    parser.add_argument("--image", required=True, type=Path, help="JPEG or PNG image.")
    parser.add_argument(
        "--config", type=Path, default=REPO_ROOT / "config.json", help="JSON configuration file."
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Upload and trigger IFTTT. Without this flag, only validate and preview.",
    )
    parser.add_argument(
        "--yes", action="store_true", help="Skip interactive confirmation; requires --publish."
    )
    parser.add_argument(
        "--allow-duplicate",
        action="store_true",
        help="Allow an exact repeat of the most recent successful text/image pair.",
    )
    return parser.parse_args()


def resolve_path(value: str, config_path: Path) -> Path:
    path = Path(value).expanduser()
    return path if path.is_absolute() else config_path.parent / path


def load_config(path: Path) -> dict[str, object]:
    path = path.expanduser().resolve()
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        fail(f"could not read config file {path}: {exc}")
    except json.JSONDecodeError as exc:
        fail(f"config file is not valid JSON: {exc}")

    required = (
        "cloudinary_cloud_name",
        "cloudinary_upload_preset",
        "ifttt_event",
        "ifttt_key_file",
        "state_file",
    )
    missing = [name for name in required if not config.get(name)]
    if missing:
        fail(f"config is missing required values: {', '.join(missing)}")

    event = str(config["ifttt_event"])
    if not event.replace("_", "").isalnum():
        fail("ifttt_event may contain only letters, numbers, and underscores")

    config["_config_path"] = path
    config["_key_path"] = resolve_path(str(config["ifttt_key_file"]), path)
    config["_state_path"] = resolve_path(str(config["state_file"]), path)
    config["max_image_mb"] = int(config.get("max_image_mb", 10))
    config["max_post_characters"] = int(config.get("max_post_characters", 280))
    return config


def load_and_validate(
    args: argparse.Namespace, config: dict[str, object]
) -> tuple[str, Path, str, bytes, str]:
    if args.text_file:
        try:
            text = args.text_file.read_text(encoding="utf-8").strip()
        except OSError as exc:
            fail(f"could not read text file: {exc}")
    else:
        text = (args.text or "").strip()

    maximum = int(config["max_post_characters"])
    if not text:
        fail("post text is empty")
    if len(text) > maximum:
        fail(f"post text is {len(text)} characters; configured limit is {maximum}")

    image = args.image.expanduser().resolve()
    if not image.is_file():
        fail(f"image does not exist: {image}")
    try:
        image_bytes = image.read_bytes()
    except OSError as exc:
        fail(f"could not read image: {exc}")
    maximum_bytes = int(config["max_image_mb"]) * 1024 * 1024
    if not image_bytes:
        fail("image is empty")
    if len(image_bytes) > maximum_bytes:
        fail(f"image is larger than {config['max_image_mb']} MB")

    mime_type = mimetypes.guess_type(image.name)[0] or ""
    if mime_type not in ALLOWED_MIME_TYPES:
        fail("image must use a .jpg, .jpeg, or .png extension")
    if mime_type == "image/png" and not image_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
        fail("file extension says PNG, but the file signature does not")
    if mime_type == "image/jpeg" and not image_bytes.startswith(b"\xff\xd8\xff"):
        fail("file extension says JPEG, but the file signature does not")

    digest = hashlib.sha256(text.encode("utf-8") + b"\0" + image_bytes).hexdigest()
    return text, image, mime_type, image_bytes, digest


def check_duplicate(state_path: Path, digest: str, allow_duplicate: bool) -> None:
    if allow_duplicate or not state_path.exists():
        return
    try:
        previous = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return
    if previous.get("digest") == digest:
        fail("exact text/image pair was the most recent successful post; use --allow-duplicate")


def multipart_body(
    fields: dict[str, str], image: Path, mime_type: str, data: bytes
) -> tuple[bytes, str]:
    boundary = f"----x-publisher-{uuid.uuid4().hex}"
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                value.encode(),
                b"\r\n",
            ]
        )
    safe_name = image.name.replace('"', "")
    chunks.extend(
        [
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="file"; filename="{safe_name}"\r\n'.encode(),
            f"Content-Type: {mime_type}\r\n\r\n".encode(),
            data,
            b"\r\n",
            f"--{boundary}--\r\n".encode(),
        ]
    )
    return b"".join(chunks), boundary


def upload_to_cloudinary(
    config: dict[str, object], image: Path, mime_type: str, data: bytes
) -> str:
    body, boundary = multipart_body(
        {"upload_preset": str(config["cloudinary_upload_preset"])}, image, mime_type, data
    )
    url = (
        "https://api.cloudinary.com/v1_1/"
        f"{config['cloudinary_cloud_name']}/image/upload"
    )
    request = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        fail(f"Cloudinary upload failed with HTTP {exc.code}: {detail}")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        fail(f"Cloudinary upload failed: {exc}")
    secure_url = payload.get("secure_url")
    if not isinstance(secure_url, str) or not secure_url.startswith("https://"):
        fail("Cloudinary response did not contain a valid secure_url")
    return secure_url


def read_ifttt_key(path: Path) -> str:
    try:
        key = path.read_text(encoding="utf-8").strip()
    except OSError as exc:
        fail(f"could not read IFTTT key file: {exc}")
    if "/with/key/" in key:
        key = key.rsplit("/with/key/", 1)[1]
    elif key.startswith("with/key/"):
        key = key.removeprefix("with/key/")
    key = key.strip("/")
    if not key or any(character.isspace() for character in key):
        fail("IFTTT key file is empty or contains whitespace")
    return key


def trigger_ifttt(config: dict[str, object], text: str, image_url: str, key: str) -> str:
    url = f"https://maker.ifttt.com/trigger/{config['ifttt_event']}/with/key/{key}"
    body = json.dumps({"value1": text, "value2": image_url}).encode("utf-8")
    request = urllib.request.Request(
        url, data=body, method="POST", headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8", errors="replace").strip()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500].replace(key, "[REDACTED]")
        fail(f"IFTTT request failed with HTTP {exc.code}: {detail}")
    except (urllib.error.URLError, TimeoutError) as exc:
        fail(f"IFTTT request failed: {str(exc).replace(key, '[REDACTED]')}")


def record_success(state_path: Path, digest: str, image_url: str) -> None:
    state_path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps({"digest": digest, "image_url": image_url}, indent=2) + "\n",
        encoding="utf-8",
    )
    os.chmod(state_path, 0o600)


def main() -> None:
    args = parse_args()
    if args.yes and not args.publish:
        fail("--yes can only be used with --publish")
    config = load_config(args.config)
    text, image, mime_type, image_bytes, digest = load_and_validate(args, config)
    state_path = Path(config["_state_path"])
    check_duplicate(state_path, digest, args.allow_duplicate)

    maximum = int(config["max_post_characters"])
    print("Post preview\n------------")
    print(text)
    print("------------")
    print(f"Characters: {len(text)}/{maximum}")
    print(f"Image: {image}")
    print(f"Image type: {mime_type}")
    print(f"Image size: {len(image_bytes):,} bytes")
    print(f"Target event: {config['ifttt_event']}")

    if not args.publish:
        print("DRY RUN: nothing was uploaded or posted.")
        return
    if not args.yes:
        confirmation = input("Type POST to upload the image and trigger IFTTT: ")
        if confirmation != "POST":
            fail("confirmation not received; nothing was uploaded or posted")

    key = read_ifttt_key(Path(config["_key_path"]))
    print("Uploading image to Cloudinary...")
    image_url = upload_to_cloudinary(config, image, mime_type, image_bytes)
    print(f"Image uploaded: {image_url}")
    print("Triggering IFTTT...")
    response = trigger_ifttt(config, text, image_url, key)
    record_success(state_path, digest, image_url)
    print(f"IFTTT accepted the event: {response or '(empty response)'}")


if __name__ == "__main__":
    main()
