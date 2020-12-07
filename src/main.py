# coding=utf8

import fileutil
import pic_handle
import response

import json
from linebot import LineBotApi
import os
from linebot.webhook import WebhookHandler
from linebot import *
from flask import Flask, request, Response
import traceback
import sys
from linebot.models import *
# from linebot.models.send_messages import *
import tempfile
from flask.helpers import send_from_directory



# ###################################################################################



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
app = Flask(__name__, static_folder='static')


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

# 靜態檔案資料夾
@app.route('/static/<path:path>')
def send_file(path):
    print('Try to reach FILE: ', path)
    return send_from_directory('static', path)

@app.route('/gettemplist')
def gettemplist():
    print('Try to reach TEMP_LIST')
    s = ''
    for root, dirs, files in os.walk(fileutil.dir_temp):
        for f in files:
            fullpath = os.path.join(root, f)
            s += fullpath + '<br>\r\n'
    return s

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
        # print(body, signature)
        webhook_handler.handle(body, signature)
        return 'OK'
    except Exception:
        # print(e)
        traceback.print_exc()
        app.logger.error( traceback.format_exc() )
        return Response('oh no i fucked', 500)


############################################################################################################

# onMessage
@webhook_handler.add(MessageEvent, message=TextMessage)
def onMessage(event):
    # 
    print("[GET TXT]", event.message, flush=True)    
    # print( event.message.type )

    # 製作回覆
    message = response.generate_response_from_directories( str(event.message.text) )
    # message = TextSendMessage(text="郭")


    # 發送回覆
    linebot_api.reply_message(event.reply_token, message)
    # print("--------------", flush=True)    


@webhook_handler.add(MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
def handle_content_message(event):
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
    elif isinstance(event.message, VideoMessage):
        ext = 'mp4'
    elif isinstance(event.message, AudioMessage):
        ext = 'm4a'
    else:
        return

    # 拿訊息
    message_content = linebot_api.get_message_content(event.message.id)

    # 下載 (暫暫存)
    with tempfile.NamedTemporaryFile(dir=fileutil.dir_temp, prefix=ext+'-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name      
    # 加上副檔名
    dist_path = tempfile_path + '.' + ext
    # dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)

    # 試試看處理圖片
    new_path = pic_handle.pic_handle(dist_path)
    new_name = os.path.basename(new_path)
    

    # 傳送！
    linebot_api.reply_message(
        event.reply_token, [
            # TextSendMessage(text='檔案已儲存'),
            TextSendMessage( text=request.host_url + os.path.join('static', 'temp', new_name) )
        ]);



@webhook_handler.default()
def default(event):
    print('[DEFAULT_EVENT_HANDLER] ', event, flush=True)


############################################################################################################


# 伺服器開啟 Link Start!
if __name__ == "__main__":
    print("===== Link Start! =====")  

    useport = int(os.environ.get("PORT", 5000))    
    
    fileutil.mkdirs(".output")
    # handler = TimedRotatingFileHandler(
    #     fileutil.abs_path(".output/linebot.log"), 
    #     when="D", 
    #     interval=1, 
    #     backupCount=15,
    #     encoding="UTF-8", 
    #     delay=False, 
    #     utc=True
    # )
    # handler = 
    # app.logger.addHandler(handler)
    
    app.run(debug=True, host='0.0.0.0', port=useport)