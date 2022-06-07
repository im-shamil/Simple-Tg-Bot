from pyrogram import filters
from bot.config import channel_username

def enforce_filter (_, __, m):

  members = []
  
  for i in __.get_chat_members (channel_username):
    members.append (i.user.id)
  
  if m.chat.id not in members:
    return True

  else:
    return False

enforce = filters.create (enforce_filter)
