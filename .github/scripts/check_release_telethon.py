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
import urllib.error
import urllib.request
from html import escape
from pathlib import Path

from telethon import TelegramClient, errors as tg_errors
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

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            releases = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"::error::GitHub API HTTP {e.code}: {e.reason}")
        sys.exit(1)
    except (json.JSONDecodeError, OSError) as e:
        print(f"::error::Failed to fetch GitHub releases: {e}")
        sys.exit(1)

    if not releases:
        print("No releases yet — exiting normally")
        sys.exit(0)

    return releases[0]


def download_assets(release_data: dict, dest_dir: str) -> list[str]:
    """Download all release assets into *dest_dir*.  Returns list of local paths."""
    assets = release_data.get("assets", [])
    if not assets:
        print("No assets to download")
        return []

    paths: list[str] = []
    for a in assets:
        url = a["browser_download_url"]
        name = a["name"]
        local_path = Path(dest_dir) / name
        size_mb = round(a["size"] / 1_048_576, 1)

        print(f"Downloading  {name}  ({size_mb} MB) …")
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
            with urllib.request.urlopen(req, timeout=120) as resp:
                with open(local_path, "wb") as f:
                    f.write(resp.read())
            print(f"Downloaded  {name}  → {local_path}")
            paths.append(str(local_path))
        except Exception as e:
            print(f"::warning::Failed to download asset {name}: {e}")

    return paths


# ---------------------------------------------------------------------------
# Telethon notification
# ---------------------------------------------------------------------------


async def notify(release_data: dict, asset_paths: list[str]) -> None:
    """Send HTML notification message + asset files to every chat in TG_CHAT_ID."""
    chat_ids = [c.strip() for c in TG_CHAT_ID.split(",") if c.strip()]
    if not chat_ids:
        print("::error::TG_CHAT_ID is empty after splitting")
        sys.exit(1)

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
        print(f"::error::Telegram auth failed — check TG_API_ID / TG_API_HASH / TG_BOT_TOKEN: {e}")
        sys.exit(1)
    print("Telethon client started")
    try:
        for raw_cid in chat_ids:
            # Numeric chat ID or @username (strip @ for Telethon)
            entity: int | str
            try:
                entity = int(raw_cid)
            except ValueError:
                entity = raw_cid.lstrip("@")

            try:
                # 1. Send notification text
                await client.send_message(entity, text, parse_mode="html")
                print(f"Notification sent to  {raw_cid}")

                # 2. Send each downloaded asset as a document
                for ap in asset_paths:
                    fname = Path(ap).name
                    fsize = Path(ap).stat().st_size
                    if fsize == 0:
                        print(f"::warning::Skipping empty asset: {fname}")
                        continue
                    fsize_mb = round(fsize / 1_048_576, 1)

                    # Telegram bot file size limit via MTProto is 50 MB
                    MAX_BOT_FILE_MB = 50
                    if fsize_mb > MAX_BOT_FILE_MB:
                        print(
                            f"::warning::Skipping {fname} ({fsize_mb} MB) "
                            f"— exceeds {MAX_BOT_FILE_MB} MB bot limit"
                        )
                        continue

                    try:
                        await asyncio.wait_for(
                            client.send_file(
                                entity,
                                ap,
                                caption=fname,
                                force_document=True,
                            ),
                            timeout=300,  # 5 min per file upload
                        )
                        print(f"Asset  {fname} ({fsize_mb} MB)  sent to  {raw_cid}")
                    except asyncio.TimeoutError:
                        print(f"::error::Upload timeout for {fname} ({fsize_mb} MB) — skipping")
                        continue

            except tg_errors.FloodWaitError as e:
                print(
                    f"::error::Flood wait {e.seconds}s on {raw_cid}"
                    " — skipping remaining chats"
                )
                break
            except tg_errors.RPCError as e:
                print(f"::error::Telegram RPC error for {raw_cid}: {e}")
                continue
            except ValueError as e:
                print(f"::error::Invalid chat ID '{raw_cid}': {e}")
                continue
            except Exception as e:
                print(f"::error::Failed to send to {raw_cid}: {e}")
                continue
    finally:
        await client.disconnect()  # type: ignore[misc]
        print("Telethon client disconnected")


# ---------------------------------------------------------------------------
# Entry-point
# ---------------------------------------------------------------------------


async def main() -> None:
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
        await notify(release_data, asset_paths)

    with open(DATA_FILE, "w") as f:
        f.write(latest_updated + "\n")
    print(f"Release data persisted: {latest_updated[:19]}")


if __name__ == "__main__":
    asyncio.run(main())
