# LineBot-ElderlyPicGenerator
### 109-1 NCU AI人工智慧導論 期末專案 

[TOC]

## 講師
<!-- ![](https://marketing-prd.s3.amazonaws.com/goodjob/bigdata/imgs/teacher_%E6%9D%8E%E7%A7%89%E9%B4%BB%E8%80%81%E5%B8%AB.jpg) -->
![](https://avatars2.githubusercontent.com/u/7921358?s=460&u=af4a62f3f2233613325f8268b79e707c439c756e&v=4)

https://github.com/BingHongLi


## 專案介紹
待補

## 使用方式
待補

## 開發指南

### 開發環境
- python 3.9

### 建立環境
- 在根目錄建立一個 `.env` 檔案
- 裡面的設定內容請參考 [settings.py] 有的環境變數
- `.env` 範例
```
PORT=3000
LINEBOT_CHANNEL_ACCESS_TOKEN=XXXXXXXXXX
LINEBOT_CHANNEL_SECRET=XXXXXXXXXXX
```

### Building and Running
```
docker build --tag line_bot_elderly .
docker run -p 3000:3000 --env-file .env line_bot_elderly
```
要在裡面執行一些東西的話就
```
docker ps
docker exec -it 那個Container的ID bash
```

### Deploying to Heroku
after 
```
heroku login
heroku container:login
```
, do
```
heroku container:push web
heroku container:release web
```



## Credits
### Fonts
- [台北黑體](https://sites.google.com/view/jtfoundry)