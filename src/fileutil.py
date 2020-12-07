
import os



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


############################################################################################

# 輸出資料夾
# dir_output = abs_path('static/output')
# mkdirs(dir_output)

# 暫存檔案夾
dir_temp = abs_path('static/temp')
mkdirs(dir_temp)
dir_resp = abs_path('response')