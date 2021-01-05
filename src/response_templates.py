from linebot.models import *
import random

def flex_acoustic_message(msg:str, submsg:str, subsubmsg:str, bgUrl:str=''):
  """
  製作非常漂亮的訊息
  如果沒有bgurl，會隨機產生長輩愛用bg
  """
  if not bgUrl:
    bgs = [
      'https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366321.jpg',
      'https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366325.jpg',
      'https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366326.jpg',
      'https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366327.jpg',
      'https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366328.jpg',
      'https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366329.jpg']
    bgUrl = random.choice(bgs)

  content = {
                "type": "bubble",
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "image",
                      "url": bgUrl,
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "1:1",
                      "gravity": "center"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [],
                      "position": "absolute",
                      "background": {
                        "type": "linearGradient",
                        "angle": "0deg",
                        "endColor": "#00000000",
                        "startColor": "#00000099"
                      },
                      "width": "100%",
                      "height": "40%",
                      "offsetBottom": "0px",
                      "offsetStart": "0px",
                      "offsetEnd": "0px"
                    },
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "box",
                              "layout": "horizontal",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": msg,
                                  "size": "xl",
                                  "color": "#ffffff"
                                }
                              ]
                            },
                            {
                              "type": "box",
                              "layout": "horizontal",
                              "contents": [
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": submsg,
                                      "color": "#ffffff",
                                      "size": "md",
                                      "flex": 0,
                                      "align": "end"
                                    },
                                    {
                                      "type": "text",
                                      "text": subsubmsg,
                                      "color": "#a9a9a9",
                                      "size": "sm",
                                      "align": "end"
                                    }
                                  ],
                                  "flex": 0,
                                  "spacing": "lg"
                                }
                              ]
                            }
                          ],
                          "spacing": "xs"
                        }
                      ],
                      "position": "absolute",
                      "offsetBottom": "0px",
                      "offsetStart": "0px",
                      "offsetEnd": "0px",
                      "paddingAll": "20px"
                    }
                  ],
                  "paddingAll": "0px"
                }
            }            
  msg = FlexSendMessage(alt_text=msg, contents=content)
  return msg            


#####################################################################################################################


def img_cor_select_pic():
  urls = ["https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366321.jpg",
          "https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366325.jpg",
          "https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366326.jpg",
          "https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366327.jpg",
          "https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366328.jpg",
          "https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366329.jpg"]


  content = {
              "type": "image_carousel",
              "columns": [
                {
                  "imageUrl": "https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366321.jpg",
                  "action": {
                    "type": "message",
                    "label": "上傳你自己的圖片！",
                    "text": "goupload"
                  }
                }
              ]
            }


  tmp = {    
          "imageUrl": "AAAAAAAAAAAAAAAAAAAAAAAAAA",
          "action": 
          {
            "type": "message",
            "label": "就決定是你了",
            "text": "AAAAAAAAAAAAAAAAAA"
          }
        }

  for url in urls:
    tmp['imageUrl'] = url
    tmp['text'] = url
    content['columns'].append(tmp)
  
  
  tmp['imageUrl'] = 'https://images.pexels.com/photos/1142950/pexels-photo-1142950.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'
  tmp['label'] = '找不到適合的圖片？重試一次！'
  tmp['text'] = 'retry'
  content['columns'].append(tmp)

  return TemplateSendMessage(alt_text='你有選圖訊息', template=content)