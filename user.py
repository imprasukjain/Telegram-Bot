from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest

api_id = '28614790'
api_hash = 'ad029aa43d050d96f955a60c963042f5'

client = TelegramClient('session', api_id, api_hash)
client.start()

# Replace 'username' with the username of the user you want to send a message to
user = client(ResolveUsernameRequest('Username'))
print(user)

client.disconnect()
