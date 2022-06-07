import json

with open ("bot/languages/replies.json", "r") as file:
  data = json.load (file)

def reply (val):

  if val not in data:

    return "I dont know what to reply please report to the admin of me"

  else:

    return data [val]
