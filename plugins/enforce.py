from pyrogram import Client as bot
from pyrogram import filters
from bot.buttons import join_grp_btn
from bot.config import channel_username
from bot.languages import lang
from bot.filters import enforce

@bot.on_message (filters.private & enforce)
async def join_ (c, m):

  await m.reply (lang.reply ("join_grp"), reply_markup = join_grp_btn)
