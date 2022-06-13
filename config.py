## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQApmm8wlVz0VGQVC-6qcjzDyAFCk0jNQP-9UtIlQ-Kottq1cwWxoT73GP28TXssY7M13c3PHy4E2nKjPF0YZBJTglO4jk6rzXHFPjxqesAYjq1HfBiPD47-UtxYP7t04QWpmRiQxkd0dJkZk46V-kMdIwhFK7D--n_QnwbldNqT0FDj8MAZbDkW0JTOqcln04EoCXp3bYf0W0EPm2MJmgAtjh8JCshY5Xe2rzG9v3t6TFfHJRtc-hpHEWwRyLDT3rTU0WO1d9ve5jXCmR7ijoqh7qU8mRIne0-v_ywBYSWDPeCmYG59JCOXYPHuLnNU-dOzODeL1s7Lx6ITy_v-6kLNAAAAAS2neqoA")
BOT_TOKEN = getenv("BOT_TOKEN", "5548068792:AAFbHkav07jFeY4H_El1RIzOpbKNEJoUepM")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "sfsfoabot")
OWNER_ID = getenv("OWNER_ID", "1854384004")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Playvideo1")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xl444")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
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
