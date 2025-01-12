from feedparser import parse
import requests
from bs4 import BeautifulSoup
import asyncio
from config import SEND_CHANNEL, TORRENT

SAVE_MSG = {}

async def magnet(bot):
    while True:
        response = requests.get("https://www.1tamilmv.legal/index.php?/forums/forum/11-web-hd-itunes-hd-bluray.xml/")
        content = response.text
        mv = parse(content)
        title = mv.entries[0]['title']
        description = mv.entries[0]['description']
        soup = BeautifulSoup(description, 'html.parser')
        if TORRENT:
            torrent_links = soup.find_all('a')
            andi = torrent_links[3]['href']
            linkt = requests.get(andi)
            file_content = io.BytesIO(linkt.content)
            file_content.name = f"{title}.torrent"
            await bot.send_document(chat_id=SEND_CHANNEL, document=file_content)
        magnet_link_tag = soup.find('a', class_='skyblue-button')
        magnet_link = magnet_link_tag['href'] if magnet_link_tag else None
        global SAVE_MSG
        if not TORRENT and not SAVE_MSG.get(magnet_link):           
            MES = f"""**Title:** `{title}`
            
**Magnet:** `{magnet_link}`"""
            await bot.send_message(chat_id=SEND_CHANNEL, text=MES)
            SAVE_MSG[magnet_link] = magnet_link
        await asyncio.sleep(1500)
