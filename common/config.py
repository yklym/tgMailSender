import os

from dotenv import load_dotenv

load_dotenv()

SERVER_PORT = int(os.environ.get('PORT', 80))
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

WH_SERVER_URL = str(os.getenv("WH_SERVER_URL")) if "WH_SERVER_URL" in list(
    os.environ.keys()) else None
