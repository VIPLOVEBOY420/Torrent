import os

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("API_ID, API_HASH, and BOT_TOKEN must be set")

print(f"API_ID: {API_ID}, API_HASH: {API_HASH}, BOT_TOKEN: {BOT_TOKEN}")
