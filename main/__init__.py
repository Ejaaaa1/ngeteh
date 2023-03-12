import os

from dotenv import load_dotenv
from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

import logging, time, sys
load_dotenv()


logging.basicos.environ.get(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", " )
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SESSION = os.environ.get("SESSION", "")
FORCESUB = os.environ.get("FORCESUB", "")
AUTH = int(os.environ.get("AUTH", ""))
MONGO_URL = os.environ.get("MONGO_URL", "")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
