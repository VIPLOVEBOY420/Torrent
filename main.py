from pyrogram import Client
from config import API_HASH, BOT_TOKEN, API_ID

print(f"API_ID: {API_ID}")
print(f"API_HASH: {API_HASH}")
print(f"BOT_TOKEN: {BOT_TOKEN}")

try:
    bot = Client(
        "Web Scraping Bot",
        plugins=dict(root="plugins"),
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
    )
    
    print("Bot running...")
    bot.run()
except Exception as e:
    print(f"An error occurred: {e}")
