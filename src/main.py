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

version = 'v.210104.74'

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
    for u in user.__userdb:
        udict = dict(u.__dict__)
        # udict = {'a':'aa'}
        if 'edit_pic_editions' in udict:
            editionStr = '['
            for edition in udict['edit_pic_editions']:
                editionStr += str(edition.__dict__) +','
            editionStr += ']'
            udict['edit_pic_editions'] = editionStr
        # print(udict)
        s += str(udict) + '\n'
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
    # print(event, flush=True)   

    # 拿使用者資料、傳入response的參數
    myuser = user.getuser(event.source.user_id)    
    msg_message = ''
    msg_attachment_path = ''    

    # 判斷附件
    attachmentExt = '' # 附件的附檔明
    if isinstance(event.message, TextMessage):
        msg_message = str(event.message.text)
        print('文字訊息：', msg_message, flush=True)  
    elif isinstance(event.message, ImageMessage):
        attachmentExt = 'jpg'
        print('圖片訊息', flush=True)  
    elif isinstance(event.message, VideoMessage):
        attachmentExt = 'mp4'
        print('影片訊息', flush=True)  
    elif isinstance(event.message, AudioMessage):
        attachmentExt = 'm4a'
        print('聲音訊息', flush=True)  
        
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


    # 製作回覆
    if msg_message == 'reset':
        myuser.state = 0
        message = TextSendMessage(text='已重設你的狀態state')


    elif msg_message == 'checkstate':
        message = TextSendMessage(text='你的狀態碼：'+str(myuser.state)+' \nUID：'+str(myuser.uid))

    elif msg_message == 'version':
        message = TextSendMessage(text='LineBot-ElderlyPicGenerator '+str(version))

    # elif msg_message == 'tmpeep110': #when demo, remove this
    #     # upload rich menu ppic, before this, register ruch menu first
    #     with open( os.path.join(fileutil.dir_resp, 'richmenu_state110', 'v2.jpg') , 'rb') as f:
    #         linebot_api.set_rich_menu_image('richmenu-87d4b4dbe02db04127c03ca06f5b9ba7', 'image/jpeg', f)
    #     message = TextSendMessage(text='ok')
    # elif msg_message == 'tmpeep112': #when demo, remove this
    #     # upload rich menu ppic, before this, register ruch menu first
    #     with open( os.path.join(fileutil.dir_resp, 'richmenu_state112', 'v2.jpg') , 'rb') as f:
    #         linebot_api.set_rich_menu_image('richmenu-063fc5e646c13b50d27811df86d7c647', 'image/jpeg', f)
        message = TextSendMessage(text='ok')

    else:
        message = response.determine_response(myuser, msg_message, msg_attachment_path, attachmentExt)

    # 發送回覆
    linebot_api.reply_message(event.reply_token, message)

    # 掛上 Rich Menu
    attach_richmenu_id = response.determine_attach_rich_menus(myuser)
    if attach_richmenu_id:
        linebot_api.link_rich_menu_to_user(event.source.user_id, attach_richmenu_id)
        print('掛上Rich Menu', attach_richmenu_id, flush=True)
    else:
        linebot_api.unlink_rich_menu_from_user(event.source.user_id)

    return;

# @webhook_handler.add(MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
# def handle_content_message(event):
    # ...

@webhook_handler.add(FollowEvent)
def onFollow(event):
    """
    使用者【關注】事件
    """
    print("使用者關注", event, flush=True) 
    myuser = user.getuser(event.source.user_id) 
    myuser.state = 1
    message = response.generate_response_from_directories('init')
    linebot_api.reply_message(event.reply_token, message)


@webhook_handler.add(PostbackEvent)
def onPostback(event):
    """
    使用者【PostBack】事件
    """
    print("使用者【PostBack】事件", event, flush=True) 
    myuser = user.getuser(event.source.user_id) 
    # TODO


@webhook_handler.default()
def default(event):
    """
    使用者【其他】事件
    """
    print('使用者【其他】事件 ', event, flush=True)


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