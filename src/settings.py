"""
從環境變數撈設定
"""
import os

# Heroku 會幫我們設好
USE_PORT =  os.environ.get("PORT", 3000)

# 
LINEBOT_CHANNEL_ACCESS_TOKEN = os.environ.get("LINEBOT_CHANNEL_ACCESS_TOKEN")
LINEBOT_CHANNEL_SECRET = os.environ.get("LINEBOT_CHANNEL_SECRET")