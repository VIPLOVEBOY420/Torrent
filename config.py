from telethon import TelegramClient

# Ensure your API credentials are strings
API_ID = os.environ.get("API_ID", "23990433")
API_HASH = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5811431199:AAGad6YjD5nC9PTgurWIbRM4krUpopevpf8")

assert isinstance(API_ID, str), "API_ID must be a string"
assert isinstance(API_HASH, str), "API_HASH must be a string"
assert isinstance(BOT_TOKEN, str), "BOT_TOKEN must be a string"

# Initialize the client
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Add your bot's functionality here
