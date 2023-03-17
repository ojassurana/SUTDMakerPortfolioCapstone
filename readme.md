# Ojas's SUTD Maker Portfolio

**SUTD Application Number:** A2301748  
**Youtube Video URL:** https://www.youtube.com/watch?v=pQJWlQmbVug  
**Telegram Bot URL:** https://t.me/ojastech_bot

My name is Ojas Surana and I am keen to be pursuing the SUTD STEP Programme. I am also keen to be pursuing a major in CSD. Inspired by the MIT Maker Portfolio, here's my own video to showcase some cool things I have made.

**At the end of the video, I made a mini "capstone project" whereby if you message my Telegram bot: https://t.me/ojastech_bot something, it automatically changes the description of my Youtube video! Do try out messaging my bot and watch Youtube video description change!**

## The Components:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_Apps_Script.svg/1024px-Google_Apps_Script.svg.png" alt="Google" width="200"/> 

I made use of google app script to host my `Code.gs` file. 

<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/telegram/telegram.png" alt="Telegram Logo" width="200"/>

I also made use of the Telegram API (obviously!) to run my Telegram Bot.

<img src="https://www.drupal.org/files/project-images/Google-API.jpg" alt="Google API" width="200"/>

Lastly, I made use of the Google Youtube API to edit the description of the Youtube video.

<img src="https://www.seekpng.com/png/detail/70-701539_flask-flask-python-png.png" alt="Flask Logo" width="100"/> 
<img src="https://upload.wikimedia.org/wikipedia/commons/d/d2/Oauth_logo.svg" alt="OAuth Logo" width="100"/>

**Note! This code does not use Flask.** But I only used it initially to obtain the OAuth token to login to the Google API every time the Youtube video description is edited.

## How does the code work?

The `code.gs` script listens for messages on it's webhook from telegram server and subsequently changes the Youtube video description. 

The moment it sees that it has received a message, it will use the OAuth token to log in to the Google API so as to edit my Youtube video description.
