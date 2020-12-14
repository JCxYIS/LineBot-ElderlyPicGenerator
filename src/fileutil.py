

import os
import tempfile
import time
import uuid



############################################################################################


def abs_path(relative_path):
    """
    combine relative path to abs path
    """
    return os.path.join( os.path.dirname(__file__),  relative_path )



def mkdirs(relative_dir_path):
    """
    把沿途的路徑建立好
    """
    if not os.path.exists( abs_path(relative_dir_path) ): # 準備好資料夾
        os.makedirs( relative_dir_path )

def create_random_fileName_in_temp_dir(ext):
    """
    在暫存資料夾產生一個隨機檔名
    ext:副檔名
    """
    return os.path.join( dir_temp, str(time.time())+str(uuid.uuid4())+"."+ext )

def temp_path_to_server_path(absTempPath):
    """
    找出暫存檔案在伺服器裡面的位置 \\ 
    目前不會判斷暫存檔案484真的在暫存資料夾
    """
    from main import request
    return request.host_url + os.path.join( 'static', 'temp', os.path.basename(absTempPath) )


############################################################################################

# 輸出資料夾
# dir_output = abs_path('static/output')
# mkdirs(dir_output)

# 暫存檔案夾
dir_temp = abs_path('static/temp')
mkdirs(dir_temp)
dir_resp = abs_path('response')
dir_fonts = abs_path('static/fonts')