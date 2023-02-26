import os
import requests
import json
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

import telepot

def change_title_content(content):
  video_id = "Define your video id here"
  with open('secret.json') as json_file: secret = json.load(json_file)
  credentials = google.oauth2.credentials.Credentials(**secret)
  youtube = googleapiclient.discovery.build(
      API_SERVICE_NAME, API_VERSION, credentials=credentials)
  message = "Kindly text my Telegram Bot www.t.me/ojastech_bot and the message will be displayed below 👇\n"
  channel = youtube.channels().list(mine=True, part='snippet').execute()
  request = youtube.videos().update(
    part='snippet',
    body={
        "id": video_id,
        "snippet": {
            "title": "Ojas SUTD Makers Portfolio",
            "categoryId": 22,
            "description": (message+content+"\n\n\n\n\n\nHope you liked my video 😄"),

        },

    }
  )
  response = request.execute()
 

def handle_message(msg):
    # Get the chat ID and message text
    chat_id = msg['chat']['id']
    message_text = msg['text']
    # Construct the reply message
    reply_text = f"Thanks! The description of my Makers Portfolio Youtube video:\nyoutube.com/watch?v=Y_Y-9aMzaOs\n\nHas been changed to: \n{message_text}"
    change_title_content(message_text)
    # Send the reply message to the user
    bot.sendMessage(chat_id, reply_text)


bot_token = "PUT_YOUR_TELEGRAM_BOT_TOKEN_HERE"
bot = telepot.Bot(bot_token)
bot.message_loop(handle_message)
# This variable specifies the name of a file that contains the OAuth 2.0
# information for this application, including its client_id and client_secret.
CLIENT_SECRETS_FILE = "clients_secret.json"

# This IS FOR OAuth 2.0 
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
while True:
    pass
