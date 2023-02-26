# Ojas's SUTD Maker Portfolio

**SUTD Application Number:** A2301748  
**Youtube Video URL:**  
**Telegram Bot URL:** https://t.me/ojastech_bot

Hi fellow people! My name is Ojas Surana and I am keen to be pursuing the SUTD STEP Programme. I am also keen to be pursuing a major in CSD. Inspired by the MIT Maker Portfolio, here's my own video to showcase some cool things I have made.

**At the end of the video, I made a mini "capstone project" whereby if you message my Telegram bot: https://t.me/ojastech_bot something, it automatically changes the description of my Youtube video! Do try out messaging my bot and watch Youtube video description change!**

## The Components:

<img src="https://www.educative.io/api/edpresso/shot/5757582081785856/image/5707702298738688" alt="AWS EC2 Logo" width="200"/> 
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBEKNwby0l9dX5fW0krQcPlGrES_m0PBBVWT7yagQikMWoQnY45yXxdSe4wks7-DPGon8&usqp=CAU" alt="Ubuntu Logo" width="100"/>

I made use of an Amazon Web Services EC2 Ubuntu Linux server to host my `main.py` Python script.

<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/telegram/telegram.png" alt="Telegram Logo" width="200"/>

I also made use of the Telegram API (obviously!) to run my Telegram Bot.

<img src="https://www.drupal.org/files/project-images/Google-API.jpg" alt="Google API" width="200"/>

Lastly, I made use of the Google Youtube API to edit the description of the Youtube video.

<img src="https://www.seekpng.com/png/detail/70-701539_flask-flask-python-png.png" alt="Flask Logo" width="100"/> 
<img src="https://upload.wikimedia.org/wikipedia/commons/d/d2/Oauth_logo.svg" alt="OAuth Logo" width="100"/>

**Note! This code does not use Flask.** But I only used it initially to obtain the OAuth token to login to the Google API every time the Youtube video description is edited.

## How does the code work?

The `main.py` script constantly pings the Telegram Bot API to see if it has received any new messages _(yes, yes, I know that Webhooks are better but I will barely have any users for this bot so pinging is fine)_.

The moment it sees that it has received a message, it will use the OAuth token to log in to the Google API so as to edit my Youtube video description.

**Note:**

Do make sure to include the `client_secret.json` file which contains the OAuth login credential.
