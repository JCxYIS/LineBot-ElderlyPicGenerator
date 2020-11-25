# coding=utf8

import json
from linebot import LineBotApi
import os
from linebot.webhook import WebhookHandler
from flask import Flask, request, Response


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

# root route
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
    except:
        Response.status_code(500)
        return 'no'


from linebot.models import MessageEvent, TextMessage

# onMessage
@webhook_handler.add(MessageEvent, message=TextMessage)
def onMessage(event):
    print(event.message)
    # 讀取本地檔案，並轉譯成消息
    # result_message_array =[]
    # replyJsonPath = event.message.text
    # result_message_array = detect_json_array_to_new_message_array(replyJsonPath)

    # # 發送
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     result_message_array
    # )


# 伺服器開啟 Link Start!
if __name__ == "__main__":
    print("===Link Start!===")  
    useport = int(os.environ.get("PORT", 5000))    
    app.run(debug=True, host='0.0.0.0', port=useport)