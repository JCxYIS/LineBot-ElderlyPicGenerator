# coding=utf8

from settings import LINEBOT_CHANNEL_ACCESS_TOKEN, LINEBOT_CHANNEL_SECRET, USE_PORT
import fileutil
import pic_handle
import response
import user

import json
import os
from linebot import LineBotApi
from linebot.webhook import WebhookHandler
from linebot.models import *
from linebot import *
from flask import Flask, request, Response
import traceback
import sys
# from linebot.models.send_messages import *
import tempfile
from flask.helpers import send_from_directory



# ###################################################################################



# ###################################################################################

# 載入設定檔
# settings = None
# with open( os.path.join( os.path.dirname(__file__),  r'settings.json') ) as json_file:
#     settings = json.load(json_file)
#     print("設定檔已讀取！")
#     print(settings)

# Line Bot APIs
linebot_api = LineBotApi( LINEBOT_CHANNEL_ACCESS_TOKEN )
webhook_handler = WebhookHandler( LINEBOT_CHANNEL_SECRET )

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


# LINE POST router
@app.route('/callback', methods=['POST'])
def callback():
    # X-Line-Signature header 
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)

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

import test

############################################################################################################

@app.route('/gettemplist')
def gettemplist():
    """
    獲取暫存資料目錄
    """
    print('===[DEBUG] Try to reach TEMP_LIST===')
    s = ''
    for root, dirs, files in os.walk(fileutil.dir_temp):
        for f in files:
            fullpath = os.path.join(root, f)
            s += fullpath + '<br>\r\n'
    return s

@app.route('/getalluser')
def getalluser():
    """
    獲取所有user資料
    """
    print('===[DEBUG] Get All User===')
    s = ''
    for u in user.userdb:
        print(u.__dict__)
        s += str(u.__dict__) + '\n'
    print('=========', flush=True)
    return s

############################################################################################################

# onMessage
@webhook_handler.add(MessageEvent) # , message=TextMessage
def onMessage(event):
    """
    使用者【文字訊息】事件
    """
    # 
    print("[GET MSG]", event, flush=True)   

    # 拿使用者資料、傳入response的參數
    myuser = user.getuser(event.source.user_id)    
    msg_message = ''
    msg_attachment_path = ''    

    # 判斷附件
    attachmentExt = '' # 附件的附檔明
    if isinstance(event.message, TextMessage):
        msg_message = str(event.message.text)
    elif isinstance(event.message, ImageMessage):
        attachmentExt = 'jpg'
    elif isinstance(event.message, VideoMessage):
        attachmentExt = 'mp4'
    elif isinstance(event.message, AudioMessage):
        attachmentExt = 'm4a'
        
    # 下載附件
    # 拿訊息
    if attachmentExt:
        message_content = linebot_api.get_message_content(event.message.id)
        # 下載 (暫暫存)
        with tempfile.NamedTemporaryFile(dir=fileutil.dir_temp, prefix=attachmentExt+'-', delete=False) as tf:
            for chunk in message_content.iter_content():
                tf.write(chunk)
            tempfile_path = tf.name      
        # 加上副檔名
        msg_attachment_path = tempfile_path + '.' + attachmentExt
        os.rename(tempfile_path, msg_attachment_path)

        # # 試試看處理圖片
        # pic_path = pic_handle.pic_handle(dist_path)
        # thm_path = pic_handle.createThumb(pic_path)

        # # 取得圖片在伺服器位置
        # server_pic_path = fileutil.temp_path_to_server_path(pic_path)
        # server_thm_path = fileutil.temp_path_to_server_path(thm_path)
        # print('Rerurn pic path=', server_pic_path,'\nthumb path=', server_thm_path, flush=True)


    # 製作回覆

    # FIXME admin tasks!
    if msg_message == 'checkstate':
        message = TextSendMessage(text='查詢狀態'+str(myuser.state)+'是你的狀態碼')

    elif msg_message == 'upload_rich_edpic':
        with open( os.path.join(fileutil.dir_resp, 'richmenu_editpic', 'richmenu_edpic.jpg') , 'rb') as f:
            linebot_api.set_rich_menu_image('edpic', 'image/jpeg', f)

    else:
        message = response.determine_response(myuser, msg_message, msg_attachment_path, attachmentExt)
    # message = response.generate_response_from_directories( str(event.message.text) )
    # message = TextSendMessage(text="郭")

    # 發送回覆
    linebot_api.reply_message(event.reply_token, message)
    # print("--------------", flush=True) 

    # 傳送！
    # linebot_api.reply_message(
    #     event.reply_token, [
    #         # TextSendMessage(text='檔案已儲存'),
    #         # TextSendMessage( text= )
    #         ImageSendMessage(
    #             original_content_url=server_pic_path,
    #             preview_image_url=server_thm_path)
    #     ]);
    return;

# @webhook_handler.add(MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
# def handle_content_message(event):
    # ...

@webhook_handler.add(FollowEvent)
def onFollow(event):
    """
    使用者【關注】事件
    """
    print("[OnFOLLOW]", event, flush=True) 
    myuser = user.getuser(event.source.user_id) 
    myuser.state = 1
    message = response.generate_response_from_directories('init')
    linebot_api.reply_message(event.reply_token, message)


@webhook_handler.add(PostbackEvent)
def onPostback(event):
    """
    使用者【PostBack】事件
    """
    print("[onPostback]", event, flush=True) 
    myuser = user.getuser(event.source.user_id) 
    # TODO


@webhook_handler.default()
def default(event):
    """
    使用者【其他】事件
    """
    print('[DEFAULT_EVENT_HANDLER] ', event, flush=True)


############################################################################################################


# 伺服器開啟 Link Start!
if __name__ == "__main__":
    print("===== Link Start! =====")  
  
    
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
    
    app.run(debug=True, host='0.0.0.0', port=USE_PORT)