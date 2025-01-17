# code by @Mrz_bots
# don't Remove credits

from pyrogram import Client
from aiohttp import web
from config import *
from tools.magnets import magnet

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Hello World!")


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="chatgpt",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "rss"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        web_app = web.Application(client_max_size=30000000)
        web_app.add_routes(routes)
        app = web.AppRunner(web_app)
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", 8080).start()
        await magnet(self)
        print(f"{me.first_name} Now Working 😘")
        
Bot().run()
