# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

# get your api_id, api_hash, token
# from telegram as described above
api_id = '28614790'                   #------------------------------> Insert Your API key
api_hash = 'ad029aa43d050d96f955a60c963042f5' #---------------------> Insert Your API hash
token = '6294156830:AAHazMVgMCnGHeuRlsoGpE5bkx2K5LIe_Wc'
message = "This message is sent by Telegram api"

# your phone number
phone = '+91'          #-------------------> Insert Your Phone number

# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('session', api_id, api_hash)

# connecting and building the session
client.connect()

# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
if not client.is_user_authorized():
    client.send_code_request(phone)

    # signing in the client
    client.sign_in(phone, input('Enter the code: '))

try:
    # receiver user_id and access_hash, use
    # my user_id and access_hash for reference
    user_id = 1422788549
    user_hash = -4889663714049590767
    receiver = InputPeerUser(1422788549, -4889663714049590767)

    # sending message using telegram client
    client.send_message(receiver, message, parse_mode='html')
except Exception as e:

    # there may be many error coming in while like peer
    # error, wrong access_hash, flood_error, etc
    print(e);

# disconnecting the telegram session
client.disconnect()
