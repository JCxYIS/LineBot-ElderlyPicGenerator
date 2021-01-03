import fileutil

from PIL import Image, ImageDraw, ImageFilter, ImageFont, JpegImagePlugin
import os
import time


######################################################


def pic_handle(pic_abspath:str, actions:list):
    """
    修圖，最終把圖片儲存在temp，並回傳(絕對)路徑\\
    """

    # 讀圖
    # picpath = os.path.join( os.path.dirname(__file__),  r'pic/cut19_worldend-2400x1602.jpg') 
    inputImg = Image.open(pic_abspath)

    # 開個新畫布
    resultImg = Image.new('RGB', inputImg.size, (0, 0, 0, 0)) # RGBA->PNG (Fat)
    resultImg.paste(inputImg, (0,0))

    # all layers
    for action in actions:

        # 加點字
        if action.operation == 'AddText':
            myFont = ImageFont.truetype( os.path.join(fileutil.dir_fonts ,  r'TaipeiSansTCBeta-Regular.ttf') , 200)           
            draw = ImageDraw.Draw(resultImg)

            draw.text( 
                xy= ( action.posx, action.posy ), 
                text= action.text, 
                fill=(action.colorr, action.colorg, action.colorb, action.colora), 
                font= myFont, 
                anchor='mm' )

        # 加點濾鏡
        elif action.operation == 'AddFilter': #TODO
            resultImg = resultImg.filter(ImageFilter.CONTOUR)
            resultImg = resultImg.effect_spread(25)

        # error!
        else:
            raise 'Invalid action defined!!!'

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




# main classes ------------------------------------------------------------------------

class PicEdition:
    """
    每一筆圖片修改的操作。不要從基底創建東西！ \\
    action: 看有什麼更改圖片的操作，如：'AddText', 'AddFilter' (注意首字大寫) \\
    """
    def __init__(self, operation:str):
        super().__init__()
        self.operation = operation
        # self.param = parameters


# PicEditionAction classes ------------------------------------------------------------------------

class PicEdition_AddText(PicEdition):
    def __init__(self, text:str, posx:float, posy:float, size:int, colorr:int, colorg:int, colorb:int, colora:int):
        super().__init__('AddText')
        self.text = text
        self.posx = posx
        self.posy = posy
        self.size = size
        self.colorr = colorr
        self.colorg = colorg
        self.colorb = colorb
        self.colora = colora

class PicEdition_AddFilter(PicEdition):
    def __init__(self, filterName:str):
        super().__init__('AddFilter')
        self.filterName = filterName