import os 
from telethon import TelegramClient

# Ensure your API credentials are strings
API_ID = os.environ.get("API_ID", "4353856")
API_HASH = os.environ.get("API_HASH", "21baea4745fd7cc26a4d38a7452f3b42")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7601646044:AAGTFKdRzL7uTB0L7lEQy4rk19T2c9QCpNI")

assert isinstance(API_ID, str), "API_ID must be a string"
assert isinstance(API_HASH, str), "API_HASH must be a string"
assert isinstance(BOT_TOKEN, str), "BOT_TOKEN must be a string"

# Initialize the client
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Add your bot's functionality here
