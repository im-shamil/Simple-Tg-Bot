from pyrogram import Client
from bot.config import api_id, api_hash, bot_token

Client (
    name = "Test",
    api_id = api_id,
    api_hash = api_hash,
    bot_token = bot_token,
    plugins = {
        "root": "plugins"
    }
).run()
