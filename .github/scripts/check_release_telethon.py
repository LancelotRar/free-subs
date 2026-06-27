#!/usr/bin/env python3
"""
Check GitHub releases and send notification + assets via Telethon (MTProto).

Uses Telethon v1 stable (TelegramClient), NOT v2 alpha.

Environment variables:
  REPO                  - GitHub repo (e.g. "fish2018/webhtv")
  DATA_FILE             - Path to persist last release updated_at
  NOTIFY_TITLE          - Display title for notification
  NOTIFY_GROUP_URL      - Telegram group invite URL
  GITHUB_TOKEN          - GitHub token (optional, for API auth)
  TG_BOT_TOKEN          - Telegram bot token (from @BotFather)
  TG_CHAT_ID            - Target chat ID(s), comma-separated (numeric or @username)
  TG_API_ID             - Telegram API ID (from https://my.telegram.org/apps)
  TG_API_HASH           - Telegram API hash (from https://my.telegram.org/apps)
  FORCE                 - "true" to re-notify even if already notified
"""

import asyncio
import json
import os
import sys
import tempfile
import time
import urllib.error
import urllib.request

from html import escape
from pathlib import Path

from telethon import TelegramClient, errors as tg_errors, utils
from telethon.sessions import StringSession

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

REPO = os.environ["REPO"]
DATA_FILE = os.environ["DATA_FILE"]
NOTIFY_TITLE = os.environ["NOTIFY_TITLE"]
NOTIFY_GROUP_URL = os.environ["NOTIFY_GROUP_URL"]
FORCE = os.environ.get("FORCE", "").lower() == "true"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

for var in ("TG_BOT_TOKEN", "TG_CHAT_ID", "TG_API_ID", "TG_API_HASH"):
    if not os.environ.get(var):
        print(f"::error::Missing required env var: {var}")
        sys.exit(1)

TG_BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
TG_CHAT_ID = os.environ["TG_CHAT_ID"]
TG_API_ID = int(os.environ["TG_API_ID"])
TG_API_HASH = os.environ["TG_API_HASH"]

# ---------------------------------------------------------------------------
# GitHub Release helpers
# ---------------------------------------------------------------------------


def get_last_updated() -> str:
    """Read persisted last-release *updated_at* from *DATA_FILE*."""
    try:
        with open(DATA_FILE) as f:
            lines = [l.strip() for l in f if l.strip()]
            return lines[-1] if lines else ""
    except (FileNotFoundError, IndexError):
        return ""


def fetch_latest_release() -> dict:
    """Fetch the latest release from the GitHub API."""
    headers = {
        "User-Agent": "GitHub-Actions",
        "Accept": "application/vnd.github+json",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    url = f"https://api.github.com/repos/{REPO}/releases?per_page=1"
    req = urllib.request.Request(url, headers=headers)

    releases: list[dict] = []
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                releases = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code >= 500 and attempt < max_attempts:
                sleep_time = 2**attempt
                print(f"GitHub API HTTP {e.code} (attempt {attempt}/{max_attempts}), retrying in {sleep_time}s …")
                time.sleep(sleep_time)
                continue
            raise RuntimeError(f"GitHub API HTTP {e.code}: {e.reason}")
        except OSError as e:
            if attempt < max_attempts:
                sleep_time = 2**attempt
                print(f"Connection error (attempt {attempt}/{max_attempts}), retrying in {sleep_time}s …")
                time.sleep(sleep_time)
                continue
            raise RuntimeError(f"Failed to fetch GitHub releases: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to fetch GitHub releases: {e}")
        else:
            break

    if not releases:
        print("No releases yet — exiting normally")
        sys.exit(0)

    return releases[0]


def download_assets(release_data: dict, dest_dir: str) -> list[str]:
    """Download .apk release assets into *dest_dir*.  Returns list of local paths."""
    assets = release_data.get("assets", [])
    apk_assets = [a for a in assets if a["name"].endswith(".apk")]
    if not apk_assets:
        print("No APK assets to download")
        return []
    if len(apk_assets) < len(assets):
        print(f"Filtered to {len(apk_assets)} APK files (skipped {len(assets) - len(apk_assets)} non-APK)")

    paths: list[str] = []
    for a in apk_assets:
        url = a["browser_download_url"]
        name = a["name"]
        local_path = Path(dest_dir) / name
        size_mb = round(a["size"] / 1_048_576, 1)

        print(f"Downloading  {name}  ({size_mb} MB) …", flush=True)
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "GitHub-Actions",
                "Accept": "application/octet-stream",
            },
        )
        if GITHUB_TOKEN:
            req.headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

        try:
            with urllib.request.urlopen(req, timeout=3600) as resp:
                with open(local_path, "wb") as f:
                    f.write(resp.read())
            print(f"Downloaded  {name}  → {local_path}", flush=True)
            paths.append(str(local_path))
        except Exception as e:
            print(f"::warning::Failed to download asset {name}: {e}")

    return paths


# ---------------------------------------------------------------------------
# Telethon notification
# ---------------------------------------------------------------------------


async def notify(release_data: dict, asset_paths: list[str]) -> bool:
    """Send HTML notification message + asset files to every chat in TG_CHAT_ID.

    Returns True if all chats were notified successfully, False otherwise.
    """
    chat_ids = [c.strip() for c in TG_CHAT_ID.split(",") if c.strip()]
    if not chat_ids:
        raise ValueError("TG_CHAT_ID is empty after splitting")

    # --- build message text ---
    rel_name = escape(release_data.get("name") or release_data["tag_name"])
    pub_date = release_data["published_at"][:10]
    rel_url = release_data["html_url"]

    text = (
        f"🚀<b>{NOTIFY_TITLE} 新版本发布！</b>\n\n"
        f'📢<a href="{NOTIFY_GROUP_URL}">TG讨论群</a>\n\n'
        f"🌀<b>版本：</b>{rel_name}\n"
        f"🍾<b>发布时间：</b>{pub_date}\n"
        f'🔗<a href="{rel_url}">查看完整 Release 日志</a>'
    )

    # --- Telethon client ---
    # NOTE: Do NOT use `async with TelegramClient(...)` — its `__aenter__`
    # calls `self.start()` with no arguments, which would fall back to
    # interactive phone/token input (impossible in CI).
    # Instead, manage start/disconnect explicitly.
    print("Starting Telethon client …")
    # StringSession: zero-disk session, no .session file left behind in CI
    # connection_retries: handle transient network failures
    client = TelegramClient(
        StringSession(), TG_API_ID, TG_API_HASH,
        connection_retries=3,
    )
    try:
        await client.start(bot_token=TG_BOT_TOKEN)  # type: ignore[misc]
    except tg_errors.RPCError as e:
        raise RuntimeError(f"Telegram auth failed — check TG_API_ID / TG_API_HASH / TG_BOT_TOKEN: {e}")
    print("Telethon client started")
    all_ok = True
    try:
        for raw_cid in chat_ids:
            # Numeric chat ID or @username (strip @ for Telethon)
            entity: int | str
            try:
                entity = int(raw_cid)
            except ValueError:
                entity = raw_cid.lstrip("@")

            try:
                # Send all assets as a single grouped message (media group).
                # Telethon's send_file with a list uses messages.sendMultiMedia,
                # which bundles multiple documents into one message with a shared caption.
                valid_paths = [ap for ap in asset_paths if Path(ap).stat().st_size > 0]
                if valid_paths:
                    print(f"Uploading {len(valid_paths)} assets in parallel …", flush=True)
                    try:
                        # Step 1: Upload all files concurrently to Telegram CDN
                        def progress_callback(sent: int, total: int) -> None:
                            pct = sent * 100 // total
                            sent_mb = sent / 1_048_576
                            total_mb = total / 1_048_576
                            print(f"  Upload progress: {sent_mb:.1f}/{total_mb:.1f} MB ({pct}%)", flush=True)

                        uploaded = await asyncio.wait_for(
                            asyncio.gather(
                                *[client.upload_file(p, progress_callback=progress_callback) for p in valid_paths]
                            ),
                            timeout=3600,
                        )
                        print("All assets uploaded, sending media group …", flush=True)
                        # Step 2: Build InputMediaUploadedDocument with attributes
                        # from original file paths (bare InputFile lacks filename/mime).
                        from telethon.tl import types as _tg_types

                        media_entries = []
                        for path, uf in zip(valid_paths, uploaded):
                            attrs, mime = utils.get_attributes(path, force_document=True)
                            media_entries.append(_tg_types.InputMediaUploadedDocument(
                                file=uf,
                                mime_type=mime,
                                attributes=attrs,  # type: ignore[arg-type]
                                force_file=True,
                            ))

                        # Send media group without caption so all 4 files render
                        # as a clean album (2×2 grid), then send the text as a
                        # separate message below the album.
                        await client.send_file(entity, media_entries, caption="")
                        print(f"Assets sent to  {raw_cid}", flush=True)
                        await client.send_message(entity, text, parse_mode="html")
                        print(f"Text message sent to  {raw_cid}", flush=True)
                    except asyncio.TimeoutError:
                        print(f"::error::Upload timeout for assets — skipped", flush=True)
                        all_ok = False
                else:
                    # No valid assets — plain text message
                    await client.send_message(entity, text, parse_mode="html")
                    print(f"Notification sent to  {raw_cid} (no assets)", flush=True)

            except tg_errors.FloodWaitError as e:
                print(
                    f"::error::Flood wait {e.seconds}s on {raw_cid}"
                    " — skipping remaining chats"
                )
                all_ok = False
                break
            except tg_errors.RPCError as e:
                print(f"::error::Telegram RPC error for {raw_cid}: {e}")
                all_ok = False
                continue
            except ValueError as e:
                print(f"::error::Invalid chat ID '{raw_cid}': {e}")
                all_ok = False
                continue
            except Exception as e:
                print(f"::error::Failed to send to {raw_cid}: {e}")
                all_ok = False
                continue
    finally:
        await client.disconnect()  # type: ignore[misc]
        print("Telethon client disconnected")

    return all_ok


# ---------------------------------------------------------------------------
# Entry-point
# ---------------------------------------------------------------------------


async def main() -> None:
    try:
        last_updated = get_last_updated()
        release_data = fetch_latest_release()
        latest_updated = release_data.get("updated_at", "")
        rel_name = release_data.get("name") or release_data["tag_name"]

        print(
            f"Last Updated: {last_updated}  |  "
            f"Latest Updated: {latest_updated}  |  "
            f"Release: {rel_name}  |  Force: {FORCE}"
        )

        if not FORCE and latest_updated == last_updated:
            print("No new release — exiting")
            sys.exit(0)

        print("New release found, proceeding …")

        # Download assets to tmpdir, then notify
        with tempfile.TemporaryDirectory(prefix="gh_assets_") as tmpdir:
            asset_paths = download_assets(release_data, tmpdir)
            ok = await notify(release_data, asset_paths)
            if not ok:
                print("::error::Notification failed — will retry on next run")
                sys.exit(1)

        with open(DATA_FILE, "w") as f:
            f.write(latest_updated + "\n")
        print(f"Release data persisted: {latest_updated[:19]}")
    except (RuntimeError, ValueError) as e:
        print(f"::error::{e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
