from linebot.models import *

def flex_acoustic_message(msg:str, submsg:str, subsubmsg:str, bgUrl:str=''):
  """
  製作非常漂亮的訊息
  如果沒有bgurl，會隨機產生長輩愛用bg
  """
  if not bgUrl:
    # TODO
    bgUrl = 'https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366329.jpg'

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
              },
              {
                "imageUrl": "https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366325.jpg",
                "action": {
                  "type": "postback",
                  "label": "就決定是你了!",
                  "text": "pic_2",
                  "data": "pic_3JPG"
                }
              },
              {
                "imageUrl": "https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366326.jpg",
                "action": {
                  "type": "postback",
                  "label": "就決定是你了!",
                  "text": "pic_3",
                  "data": "pic_3"
                }
              },
              {
                "imageUrl": "https://storage.googleapis.com/kirito-1585904519813.appspot.com/avatars/oberon3.webp",
                "action": {
                  "type": "message",
                  "label": "就決定是你了!",
                  "text": "動作 4"
                }
              },
              {
                "imageUrl": "https://storage.googleapis.com/kirito-1585904519813.appspot.com/avatars/oberon3.webp",
                "action": {
                  "type": "message",
                  "label": "就決定是你了!",
                  "text": "動作 5"
                }
              },
              {
                "imageUrl": "https://storage.googleapis.com/kirito-1585904519813.appspot.com/avatars/oberon3.webp",
                "action": {
                  "type": "message",
                  "label": "就決定是你了!",
                  "text": "動作 6"
                }
              },
              {
                "imageUrl": "https://storage.googleapis.com/kirito-1585904519813.appspot.com/avatars/oberon3.webp",
                "action": {
                  "type": "message",
                  "label": "就決定是你了!",
                  "text": "動作 7"
                }
              },
              {
                "imageUrl": "https://storage.googleapis.com/kirito-1585904519813.appspot.com/avatars/oberon3.webp",
                "action": {
                  "type": "message",
                  "label": "就決定是你了!",
                  "text": "動作 8"
                }
              },
              {
                "imageUrl": "https://storage.googleapis.com/kirito-1585904519813.appspot.com/avatars/oberon3.webp",
                "action": {
                  "type": "message",
                  "label": "就決定是你了!",
                  "text": "動作 9"
                }
              },
              {
                "imageUrl": "https://github.com/JCxYIS/LineBot-ElderlyPicGenerator/raw/main/samplepics/366329.jpg",
                "action": {
                  "type": "message",
                  "label": "找不到想要的圖？下一頁！",
                  "text": "動作 10"
                }
              }
            ]
          }
  return TemplateSendMessage(alt_text='選擇功能(去用智會手ㄐ啦)', template=content)