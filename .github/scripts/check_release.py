import json
import os
import sys
import urllib.error
import urllib.request
from html import escape

REPO = os.environ["REPO"]
DATA_FILE = os.environ["DATA_FILE"]
NOTIFY_TITLE = os.environ["NOTIFY_TITLE"]
NOTIFY_GROUP_URL = os.environ["NOTIFY_GROUP_URL"]
FORCE = os.environ.get("FORCE", "").lower() == "true"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

for var in ("TG_BOT_TOKEN", "TG_CHAT_ID"):
    if not os.environ.get(var):
        print(f"::error::Missing required env var: {var}")
        sys.exit(1)

last_id = 0
try:
    with open(DATA_FILE) as f:
        last_id = int(f.read().strip())
except Exception:
    pass

api_headers = {
    "User-Agent": "GitHub-Actions",
    "Accept": "application/vnd.github+json",
}
if GITHUB_TOKEN:
    api_headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

url = f"https://api.github.com/repos/{REPO}/releases?per_page=1"
req = urllib.request.Request(url, headers=api_headers)
try:
    with urllib.request.urlopen(req) as resp:
        releases = json.loads(resp.read())
except urllib.error.HTTPError as e:
    print(f"::error::GitHub API HTTP {e.code}: {e.reason}")
    sys.exit(1)
except Exception as e:
    print(f"::error::Failed to fetch GitHub releases: {e}")
    sys.exit(1)

if not releases:
    print("No releases yet — exiting normally")
    sys.exit(0)

data = releases[0]

latest_id = data["id"]
print(f"Last ID: {last_id}, Latest ID: {latest_id}, Force: {FORCE}")

if not FORCE and latest_id <= last_id:
    print("No new release")
    sys.exit(0)

print("New release found, sending notification…")

rel_name = escape(data.get("name") or data["tag_name"])
pub_date = data["published_at"][:10]
rel_url = data["html_url"]

assets_lines = []
for a in data.get("assets", []):
    size_mb = round(a["size"] / 1_048_576, 1)
    name = escape(a["name"])
    assets_lines.append(
        f'• <a href="{a["browser_download_url"]}">{name}</a> ({size_mb} MB)'
    )
assets_text = "\n".join(assets_lines) if assets_lines else "（无 Assets）"

text = (
    f"🚀<b>{NOTIFY_TITLE} 新版本发布！</b>\n\n"
    f'📢<a href="{NOTIFY_GROUP_URL}">TG讨论群</a>\n\n'
    f"🌀<b>版本：</b>{rel_name}\n"
    f"🍾<b>发布时间：</b>{pub_date}\n"
    f'🔗<a href="{rel_url}">查看完整 Release 日志</a>\n\n'
    f"📦<b>下载 Assets：</b>\n{assets_text}"
)

chat_ids = [c.strip() for c in os.environ["TG_CHAT_ID"].split(",") if c.strip()]
if not chat_ids:
    print("::error::TG_CHAT_ID is empty after splitting")
    sys.exit(1)

send_ok = False
for chat_id in chat_ids:
    payload = json.dumps({
        "chat_id": chat_id,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
        "text": text,
    }).encode()
    req2 = urllib.request.Request(
        f'https://api.telegram.org/bot{os.environ["TG_BOT_TOKEN"]}/sendMessage',
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req2) as resp:
            result = json.loads(resp.read())
        if not result.get("ok"):
            print(f'::error::Telegram error (chat {chat_id}): {result.get("description")}')
        else:
            print(f"Message sent to chat {chat_id}")
            send_ok = True
    except Exception as e:
        print(f"::error::Failed to send Telegram message to {chat_id}: {e}")

if not send_ok:
    print("::error::Failed to send message to all chat IDs")
    sys.exit(1)

with open(DATA_FILE, "w") as f:
    f.write(str(latest_id))
print(f"Telegram notification sent and release ID persisted: {latest_id}")
