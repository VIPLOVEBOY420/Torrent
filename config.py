import os

API_ID = os.environ.get("23990433")
API_HASH = os.environ.get("e6c4b6ee1933711bc4da9d7d17e1eb20")
BOT_TOKEN = os.environ.get("5811431199:AAGad6YjD5nC9PTgurWIbRM4krUpopevpf8")

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("API_ID, API_HASH, and BOT_TOKEN must be set")

print(f"API_ID: {API_ID}, API_HASH: {API_HASH}, BOT_TOKEN: {BOT_TOKEN}")
Make sure you set the environment varia
