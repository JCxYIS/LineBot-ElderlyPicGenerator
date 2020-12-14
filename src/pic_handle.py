import fileutil

from PIL import Image, ImageDraw, ImageFilter, ImageFont, JpegImagePlugin
import os
import time


######################################################


def pic_handle(pic_abspath):
    """
    修圖，最終把圖片儲存在temp，並回傳(絕對)路徑
    """

    # 讀圖
    # picpath = os.path.join( os.path.dirname(__file__),  r'pic/cut19_worldend-2400x1602.jpg') 
    inputImg = Image.open(pic_abspath)

    # 開個新畫布
    resultImg = Image.new('RGB', inputImg.size, (0, 0, 0, 0)) # RGBA->PNG (Fat)
    resultImg.paste(inputImg, (0,0))



    # 加點字
    # TODO
    draw = ImageDraw.Draw(resultImg)
    myFont = ImageFont.truetype( os.path.join(fileutil.dir_fonts ,  r'TaipeiSansTCBeta-Regular.ttf') , 200)
    draw.text( xy=(resultImg.width/4, resultImg.height/2), text="業力引爆AAA", fill=(128, 149, 15, 255), font=myFont, anchor='mm' )

    # 加點其他酷東西
    # TODO
    # resultImg = resultImg.filter(ImageFilter.CONTOUR)
    # resultImg = resultImg.effect_spread(25)


    # 存圖
    picSavePath = fileutil.create_random_fileName_in_temp_dir('jpg')
    resultImg.save(picSavePath)
    print("圖片已儲存！ ", picSavePath)

    # resultImg.show()
    return picSavePath


def createThumb(pic_absPath):
    """
    a
    """

    # 讀圖
    inputImg = Image.open(pic_absPath)

    # thumbing
    inputImg.thumbnail( (200, 200) ) # thumbnail() 只能進行等比例縮小，並且是以長、寬中比較小的那一個值為基準。
    
    # save
    picSavePath = fileutil.create_random_fileName_in_temp_dir('jpg')
    inputImg.save(picSavePath)
    print("預覽圖已儲存！ ", picSavePath)
    return picSavePath