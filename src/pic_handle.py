import fileutil

from PIL import Image, ImageDraw, ImageFilter, ImageFont, JpegImagePlugin
import os
import time


######################################################


"""
修圖，最終把圖片儲存在temp，並回傳(絕對)路徑
"""
def pic_handle(pic_abspath):
    # 讀圖
    # TODO 
    # picpath = os.path.join( os.path.dirname(__file__),  r'pic/cut19_worldend-2400x1602.jpg') 
    inputImg = Image.open(pic_abspath)

    # 開個新畫布
    resultImg = Image.new('RGB', inputImg.size, (0, 0, 0, 0)) # RGBA->PNG (Fat)
    resultImg.paste(inputImg, (0,0))



    # 加點字
    # TODO
    draw = ImageDraw.Draw(resultImg)
    myFont = ImageFont.truetype( os.path.join( os.path.dirname(__file__),  r'font/TaipeiSansTCBeta-Regular.ttf') , 200)
    draw.text( xy=(resultImg.width/4, resultImg.height/2), text="業力引爆AAA", fill=(128, 149, 15, 255), font=myFont, anchor='mm' )

    # 加點其他酷東西
    # TODO
    # resultImg = resultImg.filter(ImageFilter.CONTOUR)
    resultImg = resultImg.effect_spread(25)



    # 存圖
    picSavePath = os.path.join( fileutil.dir_temp,  os.path.basename(pic_abspath)+r'-'+str(time.time())+r'.jpg')
    resultImg.save(picSavePath)
    print("圖片已儲存！ Saved to ", picSavePath)

    # resultImg.show()
    return picSavePath



