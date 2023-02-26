Ojas's SUTD Maker Portfolio


**SUTD Application Number:** A2301748 <br>
**Youtube Video URL:** <br>
**Telegram Bot URL:** https://t.me/ojastech_bot

Hi fellow people! My name is Ojas Surana and I am keen to be pursing the SUTD STEP Programme. I am also keen to be pursing a major in CSD.
Inspired by by the MIT Maker Portfolio, here's my own video to show case some cool things I have made. 

At the end of the video I made a mini "capstone project" where by if you message my Telegram bot: https://t.me/ojastech_bot something, it<br>
automatically changes the description of my Youtube video! Do try out messaging my bot and the Youtube video description change!


The Components:
<br>
![AWS EC2 Logo](https://www.educative.io/api/edpresso/shot/5757582081785856/image/5707702298738688) ![Ubuntu Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBEKNwby0l9dX5fW0krQcPlGrES_m0PBBVWT7yagQikMWoQnY45yXxdSe4wks7-DPGon8&usqp=CAU)<br>
I made use of an Amazon Web Services EC2 Ubuntu Linux server to host my main.py Python script. 
<br><br>
![Telegram Logo](https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/telegram/telegram.png) <br>
I also made of the Telegram API (obviously!) to run my Telegram Bot. <br><br>
![Google API](https://www.drupal.org/files/project-images/Google-API.jpg) <br>
Lastly, I made use of the Google Youtube API to edit the description of the Youtube
<br><br>
![Flask Logo](https://www.seekpng.com/png/detail/70-701539_flask-flask-python-png.png)
![OAuth Logo](https://upload.wikimedia.org/wikipedia/commons/d/d2/Oauth_logo.svg)
NOTE! THIS CODE DOES NOT USE FLASK. But I only used it initially to obtain the OAuth token to login to the Google API everytime the Youtube video description is edited.
<br>How does the code works: <br><br>
The main.py script constantly pings the Telegram Bot API to see if it has received any new messages _(yes yes I know that Webhooks are better but I will barely have any users for this bot so pinging is fine)_
<br>
The moment it sees that it has received a message, it will use the OAuth token to login to the Google API so as to edit my Youtube video description. 
<br>

Note:
<br>
Do make sure to include the clients_secret.json file which contain the OAuth login credential.
