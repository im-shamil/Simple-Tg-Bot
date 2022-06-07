from pyrogram import Client as bot
from pyrogram import filters
from bot.buttons import join_grp_btn
from bot.config import channel_username
from bot.languages import lang

@bot.on_message (filters.private & filters.command ("start"))
async def start_ (c, m):

  await m.reply (lang.reply ("start").format (m.chat.first_name))  
