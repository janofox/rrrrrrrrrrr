## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAD1ELFoFthKvBYag1I4oRVG37g_Uytm9WiO69vRbb5mVl2JHO2MH_ShfZC0eCupWvGJA2s9qFtZp1icCfueVU_J1ojVWVty56mJnQWdcH8Ula6lx_TQihsL1yG1alLTj3bK_uVG4g89KcFZQMgIqGvc6NUN1Xl8Xt6izHRywCMacdOz0WfioHUWYIK7MXZDxI9Sz4q28CVpxorcpivtcwEbfk3qCKDLXdxcfUbkMG4hmE2-lR1jRcsUwalK4S9inAvXThq7-de8VP7y--ov0bqqddADIpSktOuaGGZ34fzzoP4n_IAYPUDJ0XhhQEfMPk_wW5vaHSwkyOMWWSB4MotAAAAATn0DzYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5422337994:AAEvTws1mqwTf1GIHzfLqW3I0BhPxhFLUV8")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "UBPP6")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "YYIYY4BoT")
OWNER_ID = getenv("OWNER_ID", "5383415297")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "UBPP6")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ZZSZ6")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "L_B_4")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5383415297").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/46fa55b49b85c084159ce.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/466de30ee0f9383c8e09e.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
