## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAW9cD7pDAXMZsjTji_MEtHccU7ceFc2G3t1JzzKP37Ur3fDakzQYbbgphU80_xtjFOgpHlq0IXH4n9inZJ65neEd4lpyGc5thLw8eFGKhCJKSm0frZi9BFfzZb2yEOhauABpwGOT_Zh4GIiQUw_S-USW1TNBPi5vJkH9ZRKjUA7P5LFHX6mnxdzdXibchlk3zvtFsIuEkYk7TsZpHp84BOCpofHOLf6O5tmYc27XW-T2L79dQzWZGHfB82ZH3IX6mZsNEczxcq22tgfkKRqIaAjgdtF3A46OF_lQbimN9nXZqP_vDTKJt_icGlFXyzLIa88qH-nUux3buSKY04qQCyAAAAATqRNTEA")
BOT_TOKEN = getenv("BOT_TOKEN", "5401619253:AAExuHqkxZoTttgS9csJNAQInSh5zRF_bdM")
BOT_NAME = getenv("BOT_NAME", "𝗺𝗨𝗦𝗜𝗖 𝗝𝗮𝗡𝗢 𖤍")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "jano")
OWNER_USERNAME = getenv("OWNER_USERNAME", "J_A_N_U_O_1")
ALIVE_NAME = getenv("ALIVE_NAME", "jano")
BOT_USERNAME = getenv("BOT_USERNAME", "llllll_M_llllll_bot")
OWNER_ID = getenv("OWNER_ID", "5411694700")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ljl_a_lnl")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "akd444s")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "akd444s")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5411694700").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "# / ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/6e2e0559f154fbe12735c.jpg")
