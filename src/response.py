

import os
from fileutil import dir_resp
from linebot.models import *
import json



# 
def generate_response_from_directories(reqDirName):
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
        return TextSendMessage(text="林北老灰啊聽毋啦")


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
        raise BaseException("爛json格式")

            # 回傳
    return returnArray