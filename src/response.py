import os
from fileutil import dir_resp

def generate_response(req):
    print('a')

def generate_response_from_directories(reqDirName):
    dirName = os.path.join(dir_resp, reqDirName)
    if os.path.exists(dirName):
        print("Response Dir Name Exist! ", dirName)
    else:
        print("Response Dir Name NOT Exist! ", dirName)
        return None