

import os
from fileutil import dir_resp
from linebot.models import *


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
            f = open(replyJsonPath, "r")
            return f.read()
        else:
            print("[WARNING] 回應資料夾裡面不存在 reply.json！ ", replyJsonPath)
            return TextSendMessage(text="出代誌阿啦 緊去call-in開花者拉 卡緊")

    else:
        print("Response Dir Name NOT Exist! ", dirName)
        return TextSendMessage(text="林北老灰啊聽毋啦")