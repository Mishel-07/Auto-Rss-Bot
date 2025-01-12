# code by @Mrz_bots
# don't Remove credits

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from aiohttp import web
from mishal import web_server 
from os import environ

API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="chatgpt",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "mishal"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", 8080).start()
        print(f"{me.first_name} Now Working 😘")
        
Bot().run()
