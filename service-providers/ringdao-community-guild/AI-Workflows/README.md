# Post text and an image to X with Cloudinary and IFTTT

This project is a small, dependency-free Python tool that posts approved text and one image to X. It is designed for beginners and for people who want an AI assistant to walk them through setup safely.

```text
text + local image
        ↓
Cloudinary uploads the image and returns a public HTTPS URL
        ↓
IFTTT receives the text and image URL through a Webhook
        ↓
IFTTT publishes the post to your connected X account
```

## Important: IFTTT Pro is required

You need an **IFTTT Pro or Pro+ subscription**. The minimum required tier is **IFTTT Pro**.

The Free plan does not include the Webhooks service used by this project, and X actions are also Pro features. Pro+ works but is not necessary for this workflow.

- [IFTTT plans](https://ifttt.com/plans)
- [IFTTT Webhooks plan requirements](https://help.ifttt.com/hc/en-us/articles/115010230347-Webhooks-service-FAQ)

Do not continue until your IFTTT account is on the Pro or Pro+ tier.

## What you need

- A Mac, Linux, or Windows computer with Python 3.9 or newer
- An IFTTT Pro or Pro+ account
- An X account that you are authorized to connect and post to
- A free or paid Cloudinary account
- A local clone of this repository
- A JPEG or PNG image and the text you want to post

You do **not** need to install Python packages. The publisher uses only Python's standard library.

## If you are using an AI assistant

Give your assistant this instruction:

> Read this entire README before taking action. Walk me through one setup stage at a time. Verify each stage before continuing. Never ask me to paste an IFTTT Webhooks key, webhook URL, password, API secret, or session token into chat. Never publish a post until you show me the final text and image details and I explicitly approve publishing.

### Rules for the AI assistant

An AI assistant helping with this repository should:

1. Confirm that the user has IFTTT Pro or Pro+ before beginning.
2. Explain which steps must be completed in the Cloudinary, IFTTT, and X websites.
3. Never request that a secret be pasted into a conversation.
4. Store the IFTTT key only in `.secrets/ifttt_key` with file permissions set to `600`.
5. Never print, log, summarize, or commit the secret.
6. Run a dry preview before every first live test.
7. Require explicit approval immediately before a live post.
8. Treat `--publish --yes` as authorized only when the user has approved the exact text and image.
9. Confirm Cloudinary success before triggering IFTTT.
10. Report IFTTT acceptance separately from confirmation that the post is visible on X.
11. Never delete an X post, Cloudinary asset, or local file unless the user explicitly requests it.
12. Run the tests and repository-hygiene checks before committing or pushing changes.

## Setup overview

Complete these stages in order:

- [ ] 1. Confirm IFTTT Pro
- [ ] 2. Configure Cloudinary
- [ ] 3. Connect IFTTT to X
- [ ] 4. Build the IFTTT Applet
- [ ] 5. Disable IFTTT URL shortening
- [ ] 6. Configure this repository
- [ ] 7. Store the IFTTT Webhooks key
- [ ] 8. Run the tests
- [ ] 9. Preview a test post
- [ ] 10. Publish only after approval

## 1. Confirm your IFTTT subscription

Sign in at [ifttt.com](https://ifttt.com/) and confirm that your account is on the **Pro** or **Pro+** tier.

If IFTTT asks you to upgrade when selecting Webhooks or X, complete the upgrade before continuing.

## 2. Configure Cloudinary

Cloudinary hosts the image at a public HTTPS URL that IFTTT can download.

### Create the account

1. Create or sign into a [Cloudinary account](https://cloudinary.com/).
2. Open the Cloudinary Console.
3. Record your **Cloud name**. It is an identifier, not your password or API secret.

### Create an unsigned upload preset

1. Open **Settings** in Cloudinary.
2. Find **Upload presets**.
3. Create a new preset.
4. Set its signing mode to **Unsigned**.
5. Give it a recognizable name, such as `x-posts`.
6. Configure these recommended safeguards:

   | Setting | Recommended value |
   |---|---|
   | Asset folder | `x-posts` |
   | Delivery type | `upload` / public |
   | Allowed formats | `jpg`, `jpeg`, `png` |
   | Maximum file size | 10 MB |
   | Overwrite | Off / false |
   | Use filename | On / true |
   | Unique filename | On / true |

7. Save the preset.
8. Record the **upload preset name**.

Do not put a Cloudinary API secret in this project. This workflow uses the limited unsigned preset instead.

Unsigned preset names should still be kept reasonably private. Restricting file type and size reduces abuse if the preset name is exposed.

## 3. Connect IFTTT to the correct X account

1. Sign out of any incorrect X accounts in your browser.
2. Sign into the X account that should publish the posts.
3. Open the [X service on IFTTT](https://ifttt.com/twitter).
4. Select **Connect**.
5. Review the requested permissions carefully.
6. Authorize IFTTT to post to the account.
7. Confirm that IFTTT shows the intended X account before continuing.

The connected X account controls where posts appear. Test with non-sensitive content first if you manage multiple accounts.

## 4. Build the IFTTT Applet

1. Open [IFTTT Create](https://ifttt.com/create).
2. Under **If This**, select **Webhooks**.
3. Choose **Receive a web request**.
4. Choose an event name, such as:

   ```text
   post_to_x
   ```

   Use only letters, numbers, and underscores. Record the exact capitalization.

5. Under **Then That**, select **X (Twitter)**.
6. Choose **Post a tweet with image**.
7. Set the action fields as follows:

   | X action field | Webhooks ingredient |
   |---|---|
   | Tweet text | `Value1` |
   | Image URL | `Value2` |

8. Save and enable the Applet.

The publisher sends JSON shaped like this:

```json
{
  "value1": "The approved post text",
  "value2": "https://public-image-url.example/image.png"
}
```

`Value3` is unused.

## 5. Disable IFTTT URL shortening

IFTTT shortens URLs through `ift.tt` by default. If you want X to display the recognizable destination domain:

1. Open [IFTTT Account Settings](https://ifttt.com/settings).
2. Find **URL shortening**.
3. Turn off **Auto-shorten URLs**.
4. Save or update your settings.

X will still process every clickable URL through its own `t.co` service. X does not allow that behavior to be disabled, and very long URLs may be visually truncated.

## 6. Configure this repository

### Clone and enter the workflow directory

```bash
git clone https://github.com/ringecosystem/collaboration.git
cd collaboration/service-providers/ringdao-community-guild/AI-Workflows
```

### Check Python

```bash
python3 --version
```

Python 3.9 or newer is required.

### Create your local configuration

Copy the example:

```bash
cp config.example.json config.json
```

Open `config.json` in a text editor and replace the placeholders:

```json
{
  "cloudinary_cloud_name": "your-cloud-name",
  "cloudinary_upload_preset": "your-unsigned-upload-preset",
  "ifttt_event": "post_to_x",
  "ifttt_key_file": ".secrets/ifttt_key",
  "state_file": ".state/last-post.json",
  "max_image_mb": 10,
  "max_post_characters": 280
}
```

Field meanings:

| Field | Meaning |
|---|---|
| `cloudinary_cloud_name` | Cloud name shown in your Cloudinary Console |
| `cloudinary_upload_preset` | Exact unsigned preset name |
| `ifttt_event` | Exact Webhooks event name from your Applet |
| `ifttt_key_file` | Local file containing only the Webhooks key |
| `state_file` | Local duplicate-protection record |
| `max_image_mb` | Maximum accepted local image size |
| `max_post_characters` | Conservative post-text limit |

`config.json` is ignored by Git so deployment-specific values are not committed accidentally.

## 7. Store the IFTTT Webhooks key safely

Your Webhooks key can trigger your IFTTT Applets. Treat it like a password.

Find it through the [IFTTT Webhooks service](https://ifttt.com/maker_webhooks/settings). A complete Webhooks URL resembles:

```text
https://maker.ifttt.com/trigger/EVENT_NAME/with/key/YOUR_SECRET_KEY
```

Store **only** the `YOUR_SECRET_KEY` portion. Do not include `/with/key/`, and do not paste the key into chat.

### macOS or Linux

Open Terminal, enter the repository directory, and start Bash so these commands work consistently on both macOS and Linux:

```bash
bash
mkdir -p .secrets
chmod 700 .secrets

read -rsp 'Paste only the IFTTT Webhooks key: ' IFTTT_KEY
printf '\n'

umask 077
printf '%s' "$IFTTT_KEY" > .secrets/ifttt_key
unset IFTTT_KEY

chmod 600 .secrets/ifttt_key
exit
```

Verify the file without displaying its contents on macOS:

```bash
test -s .secrets/ifttt_key && stat -f '%Sp %N' .secrets/ifttt_key
```

On Linux:

```bash
test -s .secrets/ifttt_key && stat -c '%A %n' .secrets/ifttt_key
```

Expected permissions begin with:

```text
-rw-------
```

### Windows

Use a secure local method to create:

```text
.secrets\ifttt_key
```

The file must contain only the Webhooks key, with no quotes and no surrounding spaces. Restrict the file so only your Windows user can read it.

## 8. Run the tests

```bash
python3 -m unittest discover -s tests -v
```

The tests are local-only. They do not contact Cloudinary, IFTTT, or X. All tests should report `ok` followed by `OK`.

## 9. Prepare and preview a post

Create a local directory for post assets:

```bash
mkdir -p posts
```

The `posts` directory is ignored by Git so campaign text and images are not committed accidentally.

Save the text as `posts/post.txt` and the JPEG or PNG image under `posts/`, for example `posts/image.png`.

Run a dry preview:

```bash
python3 publisher.py \
  --text-file posts/post.txt \
  --image posts/image.png
```

The output should end with:

```text
DRY RUN: nothing was uploaded or posted.
```

Check carefully:

- The target IFTTT event is correct
- The complete post text is correct
- The date and time match the image
- The URL is correct
- The character count is within the configured limit
- The selected image path is correct
- The image type and size pass validation

## 10. Publish after approval

Run:

```bash
python3 publisher.py \
  --text-file posts/post.txt \
  --image posts/image.png \
  --publish
```

The publisher shows the preview again. Nothing is sent until you type exactly:

```text
POST
```

The successful sequence looks like:

```text
Uploading image to Cloudinary...
Image uploaded: https://res.cloudinary.com/...
Triggering IFTTT...
IFTTT accepted the event: Congratulations! You've fired the EVENT_NAME event
```

IFTTT acceptance means the Applet was triggered. Open your X profile and IFTTT Activity to verify that the downstream X action completed.

For a non-interactive run that has already received explicit approval, use:

```bash
python3 publisher.py \
  --text-file posts/post.txt \
  --image posts/image.png \
  --publish \
  --yes
```

## Duplicate protection

After a successful trigger, the publisher records a hash of the text and image in `.state/last-post.json`.

If the exact same text/image pair is submitted again, the publisher stops. This helps prevent accidental duplicate posts.

To intentionally repeat a post after reviewing it, add:

```text
--allow-duplicate
```

## Security and privacy

- Never commit `.secrets/`, `.state/`, `config.json`, or `posts/`.
- Never paste the Webhooks key or complete webhook URL into an AI conversation.
- Never include a Cloudinary API secret in this project.
- Remember that Cloudinary image URLs produced by this workflow are public.
- Rotate the IFTTT Webhooks key immediately if it appears in logs, screenshots, commits, or chat.
- Regenerating the Webhooks key affects every Applet and client using that IFTTT account's key.
- Review Cloudinary assets periodically and remove unneeded uploads manually.

### Rotating the Webhooks key

1. Regenerate the key in [IFTTT Webhooks settings](https://ifttt.com/maker_webhooks/settings).
2. Replace the contents of `.secrets/ifttt_key` using the secure-input instructions above.
3. Update any other workflow that uses the old key.
4. Run a new disposable test post.

## Troubleshooting

### IFTTT returns 404 with repeated `/with/key/`

The secret file probably contains part or all of the webhook URL. Replace it with only the key after `/with/key/`.

### Cloudinary says the upload preset is missing or invalid

Check that:

- The cloud name is correct
- The preset name and capitalization are exact
- The preset signing mode is **Unsigned**
- The image format and size satisfy the preset restrictions

### Cloudinary succeeds but IFTTT fails

The uploaded Cloudinary asset may remain public even though no X post was created. Check the IFTTT event name and rotated key, then remove the unused Cloudinary asset manually if desired.

### IFTTT accepts the event but no X post appears

Open IFTTT **Activity** and inspect the Applet run. Common causes include:

- The X service needs to be reconnected
- The wrong X account is connected
- The Applet is disabled
- The X action rejected the text or media
- An IFTTT or X usage limit was reached

### The image does not appear

Confirm that `Value2` is selected as the IFTTT action's **Image URL** ingredient. The Cloudinary URL must be public and begin with `https://`.

### The post contains an `ift.tt` URL

Turn off **Auto-shorten URLs** in IFTTT Account Settings, delete the unwanted X post manually, and intentionally republish with `--allow-duplicate` after approval.

### The publisher rejects a duplicate

This is intentional. Verify that the previous X post was deleted or that repetition is desired, then add `--allow-duplicate`.

### Network or DNS errors

The computer or AI-agent sandbox needs outbound HTTPS access to:

```text
api.cloudinary.com
maker.ifttt.com
```

Enable only the minimum network access required by your environment.

## Repository checks before committing

Inspect ignored files:

```bash
git status --short --ignored
```

Search tracked content for common secret patterns:

```bash
git grep -nE '(maker\.ifttt\.com/.*/with/key/|api_secret)' -- . ':!README.md' || true
```

Run the tests again:

```bash
python3 -m unittest discover -s tests -v
```

Only then commit or push the repository.
