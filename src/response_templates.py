from linebot.models import FlexSendMessage

def flex_acoustic_message(bgUrl:str, msg:str, submsg:str, subsubmsg:str):
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