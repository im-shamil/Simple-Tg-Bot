from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.languages import lang
from bot.config import channel_username
from bot.config import base_url 

join_grp_btn = InlineKeyboardMarkup([
    [InlineKeyboardButton (text = lang.reply ("join_grp"), url = base_url.format(channel_username))]
])
