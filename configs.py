# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 21942125))
    API_HASH = os.environ.get("API_HASH", "6d412af77ce89f5bb1ed8971589d61b5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6926166118:AAGmtLftMM4KTNLrZyTb9kRNHUvU-pSWquM")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOIYBu38qyIAP0zpeORw5SAl9IlY7PbwiUVPSsOJCNG3ll_UYFvQH9pBv_8XpegWPIpfHy8CSn18kKuzJDxSZ02GxOiioB9SRQdRWV-jSPNcvZjF-l7v_Lf_Cswjjd33Hx67YaLYXdRp2lbUoE2VHblnDreaI_jeimAeoJr3wNHxYg9FcYRyR2Zr8fd7nGx8pJwkDL1dIJOpWMlMYjyBA4yGq2zd6Sdl-joJJp8ZwtTPs_Z9KfgTTlRk4dmKcw6sHeRT8xdPm1SBgKm7GZHepUvtmKBCXdbyMBL96THlNVNDfJOH1wcKOh8dMvm1q1WoUJMoxMHA5Byp1Tg5kd6mVrOCb5SM=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001953742196))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/cyniteofficial'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/cyniteofficial'>Cynite</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/cyniteofficial'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Cyniteofficial</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Cyniteofficial</a></b>
"""


