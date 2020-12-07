

import os
from fileutil import dir_resp
from linebot.models import *


# 從 Response 資料夾抓相應的 Response
def generate_response_from_directories(reqDirName):
    dirName = os.path.join(dir_resp, reqDirName)
    if os.path.exists(dirName):
        print("Response Dir Name Exist! ", dirName)
    else:
        print("Response Dir Name NOT Exist! ", dirName)
        return TextSendMessage(text="林北佬灰訝聽毋啦")