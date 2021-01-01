from fileutil import dir_resp, temp_path_to_server_path
from linebot.models import *
import response_templates

import os
from user import User
import json
import pic_handle
import fileutil


def determine_response(myuser:User, message:str, attachmentPath:str, attachmentExt:str):
    """
    製作回覆
    myuser: my user
    meesage: message, may be ''
    attachmentPath: abs path, may be ''
    attachmentExt: extension of attachment, maybe ''
    """

    if message == 'checkstate':
        return response_templates.flex_acoustic_message('查詢狀態', str(myuser.state), '是你的狀態碼')

    # 起始
    if myuser.state == 0: 
        myuser.state = 1
        return generate_response_from_directories('init')

    # 開始關注
    elif myuser.state == 1:
        if message == '開始製作長輩圖':
            myuser.state = 100
            return response_templates.img_cor_select_pic() 
    
    # 開始製作長輩圖
    elif myuser.state == 100:
        if message == 'goupload':
            myuser.state = 101
            return response_templates.flex_acoustic_message('開始上傳', '來給我你要修圖的圖片', '')       
        # TODO selected pic 
    
    # 上傳圖片
    elif myuser.state == 101:
        if attachmentPath and attachmentExt=='jpg':
            myuser.edit_pic_filepath = attachmentPath
            myuser.state = 110
            myuser.edit_pic_editions = []
            # TODO 附加quick reply之類的
            return response_templates.flex_acoustic_message( 
                '上傳成功', '好耶', '接下來來修圖吧！', temp_path_to_server_path(attachmentPath) )
    
    # 選擇功能
    elif myuser.state == 110:
        # input text
        if message == 'addText':   
            myuser.state = 111
            return response_templates.flex_acoustic_message('輸入文字', '給我你要添加的文字', '新文字編輯')  
        elif message == 'finish': # TODO
            myuser.state = 0
            return response_templates.flex_acoustic_message('完成', '感謝使用長輩圖生成器！', '！')            
    
    # 輸入文字
    elif myuser.state == 111:
        if message:
            myuser.state = 112
            myuser.edit_pic_editions.append( pic_handle.Pic_Edition('addText', message) )
            path = pic_handle.pic_handle(myuser.edit_pic_filepath, myuser.edit_pic_editions)
            thumb = pic_handle.createThumb(path)
            # TODO 附加圖文選單
            return ImageSendMessage(fileutil.temp_path_to_server_path(path), fileutil.temp_path_to_server_path(thumb))
    
    # 調整文字位置
    elif myuser.state == 112:
        # TODO
        myuser.state = 110
        return response_templates.flex_acoustic_message('todo','to0','d0')
        

    

    # default fallback
    return generate_response_from_directories('default')


# ------------------------------------------------------------------------------

def generate_response_from_directories(reqDirName) -> SendMessage:
    """
    從 Response 資料夾抓相應的 Response
    """

    dirName = os.path.join(dir_resp, reqDirName)

    # 回應資料夾存在！
    if os.path.exists(dirName):
        # print("Response Dir Name Exist! ", dirName)
        replyJsonPath = os.path.join(dirName, 'reply.json')

        # 回應資料夾裡面存在 reply.json
        if os.path.exists(replyJsonPath):
            f = open(replyJsonPath, "r").read()
            msg = parse_reply_json(f)
            return msg
        else:
            print("[WARNING] 回應資料夾裡面不存在 reply.json！ ", replyJsonPath)
            return TextSendMessage(text="出代誌阿啦 緊去call-in開花者拉 卡緊")

    else:
        print("Response Dir Name NOT Exist! ", dirName)
        return response_templates.flex_acoustic_message('我聽不懂耶', '你是不是亂搞', '林北老灰啊聽毋啦')


def parse_reply_json(replyJson):
    """
    解析reply.json，回傳相應的物件
    """

    # Get json
    jsonObj = json.loads(replyJson)
    returnArray = []

    # parse json
    message_type = jsonObj['type']

    # 轉換
    if message_type == 'text':
        returnArray.append(TextSendMessage.new_from_json_dict(jsonObj))
    elif message_type == 'imagemap':
        returnArray.append(ImagemapSendMessage.new_from_json_dict(jsonObj))
    elif message_type == 'template':
        returnArray.append(TemplateSendMessage.new_from_json_dict(jsonObj))
    elif message_type == 'image':
        returnArray.append(ImageSendMessage.new_from_json_dict(jsonObj))
    elif message_type == 'sticker':
        returnArray.append(StickerSendMessage.new_from_json_dict(jsonObj))
    elif message_type == 'audio':
        returnArray.append(AudioSendMessage.new_from_json_dict(jsonObj))
    elif message_type == 'location':
        returnArray.append(LocationSendMessage.new_from_json_dict(jsonObj))
    elif message_type == 'flex':
        returnArray.append(FlexSendMessage.new_from_json_dict(jsonObj))
    elif message_type == 'video':
        returnArray.append(VideoSendMessage.new_from_json_dict(jsonObj))
    else: 
        raise BaseException("爛json格式:"+str(message_type))

            # 回傳
    return returnArray
