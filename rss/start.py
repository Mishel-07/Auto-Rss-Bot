from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("start"))
async def start(client, message):        
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Source", url="https://github.com/Mishel-07/Auto-Rss-Bot")], [InlineKeyboardButton("Support Group", url="https://t.me/XBOTSUPPORTS")]])
    await message.reply_text(f"Hey {message.from_user.mention}, I'm an auto RSS bot. You can find my source code by clicking the button below.", reply_markup=reply_markup)
