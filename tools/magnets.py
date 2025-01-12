from feedparser import parse
import requests
from bs4 import BeautifulSoup
import asyncio
from config import SEND_CHANNEL

SAVE_MSG = {}

async def magnet(bot):
    while True:
        response = requests.get("https://www.1tamilmv.legal/index.php?/forums/forum/11-web-hd-itunes-hd-bluray.xml/")
        content = response.text
        mv = parse(content)
        title = mv.entries[0]['title']
        description = mv.entries[0]['description']
        soup = BeautifulSoup(description, 'html.parser')
        magnet_link_tag = soup.find('a', class_='skyblue-button')
        magnet_link = magnet_link_tag['href'] if magnet_link_tag else None
        global SAVE_MSG
        if not SAVE_MSG.get(magnet_link):
            MES = f"""**Title:** `{title}`
            
**Magnet:** `{magnet_link}`"""
            await bot.send_message(chat_id=SEND_CHANNEL, text=MES)
            SAVE_MSG[magnet_link] = magnet_link
        await asyncio.sleep(600)
