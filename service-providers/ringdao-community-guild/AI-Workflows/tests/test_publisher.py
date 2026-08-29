import json
from pathlib import Path
import tempfile
import unittest

import publisher


class PublisherTests(unittest.TestCase):
    def test_load_config_resolves_relative_secret_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path = root / "config.json"
            config_path.write_text(
                json.dumps(
                    {
                        "cloudinary_cloud_name": "cloud",
                        "cloudinary_upload_preset": "preset",
                        "ifttt_event": "post_to_x",
                        "ifttt_key_file": ".secrets/key",
                        "state_file": ".state/last.json",
                    }
                ),
                encoding="utf-8",
            )
            config = publisher.load_config(config_path)
            self.assertEqual(config["_key_path"], (root / ".secrets/key").resolve())
            self.assertEqual(config["_state_path"], (root / ".state/last.json").resolve())

    def test_read_key_accepts_key_only(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "key"
            path.write_text("abc123", encoding="utf-8")
            self.assertEqual(publisher.read_ifttt_key(path), "abc123")

    def test_read_key_normalizes_full_webhook_url(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "key"
            path.write_text(
                "https://maker.ifttt.com/trigger/event/with/key/abc123\n", encoding="utf-8"
            )
            self.assertEqual(publisher.read_ifttt_key(path), "abc123")

    def test_multipart_body_does_not_contain_secrets(self):
        body, boundary = publisher.multipart_body(
            {"upload_preset": "preset"}, Path("image.png"), "image/png", b"png-data"
        )
        self.assertIn(b"preset", body)
        self.assertIn(b"png-data", body)
        self.assertTrue(boundary.startswith("----x-publisher-"))


if __name__ == "__main__":
    unittest.main()
