# coding=utf8

import json
from linebot import LineBotApi
import os
from linebot.webhook import WebhookHandler
from linebot import *
from flask import Flask, request, Response
import traceback


# ###################################################################################


# 載入設定檔
settings = None
with open( os.path.join( os.path.dirname(__file__),  r'settings.json') ) as json_file:
    settings = json.load(json_file)
    print("設定檔已讀取！")
    print(settings)

# Line Bot APIs
linebot_api = LineBotApi( settings["LineBot_Channel_Access_Token"] )
webhook_handler = WebhookHandler( settings["LineBot_Channel_Secret"] )

# Flask Server
app = Flask(__name__)


# ###################################################################################

# root route
@app.route('/')
def root_route():
    return Response('There is no html to render, sorry')

# hi
@app.route('/hi')
def hi_route():
    print('hi')
    return Response('Hi')

# LINE POST router
@app.route('/callback', methods=['POST'])
def callback():
    # X-Line-Signature header 
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        print(body, signature)
        webhook_handler.handle(body, signature)
        return 'OK'
    except Exception:
        # print(e)
        traceback.print_exc()
        return Response('oh no i fucked', 500)


############################################################################################################


from linebot.models import *
# from linebot.models.send_messages import *

# onMessage
@webhook_handler.add(MessageEvent, message=TextMessage)
def onMessage(event):
    # event = MessageEvent(event)
    print(event.message)

    #
    # event.
    
    # 製作回覆
    # message = TextMessage(text="郭")
    message = ImageSendMessage(
        original_content_url='https://i.imgur.com/kcYb0PY.gif',
        preview_image_url='https://mykirito.org/link/cover.jpg'
    )

    # 發送回覆
    linebot_api.reply_message(
        event.reply_token,
        message
    )



############################################################################################################

# 伺服器開啟 Link Start!
if __name__ == "__main__":
    print("===== Link Start! =====")  
    useport = int(os.environ.get("PORT", 5000))    
    app.run(debug=True, host='0.0.0.0', port=useport)