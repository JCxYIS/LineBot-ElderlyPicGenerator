
import os




############################################################################################


dir_output = abs_path('static')
mkdirs(dir_output)
dir_temp = abs_path('static/temp')
mkdirs(dir_temp)


############################################################################################

"""
combine relative path to abs path
"""
def abs_path(relative_path):
    return os.path.join( os.path.dirname(__file__),  relative_path )


"""
把沿途的路徑建立好
"""
def mkdirs(relative_dir_path):
    if not os.path.exists( abs_path(relative_dir_path) ): # 準備好資料夾
        os.makedirs( relative_dir_path )

