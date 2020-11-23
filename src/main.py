from PIL import Image, ImageDraw, ImageFont, JpegImagePlugin
import os
import time

######################################################

debug = True
ver = 'v.201123.4'

######################################################

print('長輩圖生成 Core', ver)

# 讀圖
picpath = os.path.join( os.path.dirname(__file__),  r'pic/cut19_worldend-2400x1602.jpg') # TODO 
inputImg = Image.open(picpath)

# 開個新畫布
resultImg = Image.new('RGB', inputImg.size, (0, 0, 0, 0)) # RGBA->PNG (Fat)
resultImg.paste(inputImg, (0,0))

# 加點字
# TODO
draw = ImageDraw.Draw(resultImg)
myFont = ImageFont.truetype( os.path.join( os.path.dirname(__file__),  r'font/TaipeiSansTCBeta-Regular.ttf') , 200)
draw.text( xy=(resultImg.width/4, resultImg.height/2), text="業力引爆AAA", fill=(128, 149, 15, 255), font=myFont, anchor='mm' )


# 存圖
picSavePath = os.path.join( os.path.dirname(__file__),  r'.output', '') # 資料夾名稱
if not os.path.exists( picSavePath ): # 準備好資料夾
    print("創建輸出資料夾...")
    os.makedirs( picSavePath )
picSavePath += r'output-' + str(time.time()) + r'.jpg'

resultImg.save(picSavePath)
print("圖片已儲存！ Saved to ", picSavePath)


