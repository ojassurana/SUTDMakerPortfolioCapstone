var apiToken = "";
var appUrl   = "";
var apiUrl   = "";


// set webhook
function setWebhook(){
  var url = apiUrl + "/setwebhook?url="+appUrl;
  var res = UrlFetchApp.fetch(url).getContentText();
  Logger.log(res);
}


// handle webhook
function doPost(e){
  var webhookData = JSON.parse(e.postData.contents);
  var from = webhookData.message.from.id;
  var text = webhookData.message.text;
  var url  = apiUrl+"/sendmessage?parse_mode=HTML&chat_id="+from+"&text=Thanks! The description of my Makers Portfolio Youtube video has been changed to: "+text;
  updateTitle(text);
  var opts = {"muteHttpExceptions": true}
  UrlFetchApp.fetch(url, opts).getContentText();
}


function doGet(e){
  return ContentService.createTextOutput("Method GET not allowed");
}

function updateTitle(title) {
  
  var videoID = 'Y_Y-9aMzaOs'; //   
  var part = 'snippet,statistics';
  var params = {'id': videoID};
  
  var response = YouTube.Videos.list(part, params);
  var video = response.items[0];
  video.snippet.description = "Kindly text my Telegram Bot www.t.me/ojastech_bot and the message will be displayed here 👉 "+title;
  
  try{
    YouTube.Videos.update(video, part); // 50 units
    
  }catch(e){

  }
  
}
