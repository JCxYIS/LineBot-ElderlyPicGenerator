FROM tensorflow/tensorflow:1.14.0-py3  
# FROM python:3.9-slim

ENV APP_HOME /app

WORKDIR $APP_HOME    
ADD /src /app
ADD https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5 /app/ai_model/model.h5

RUN apt-get update
RUN apt-get install sudo
RUN sudo apt update
RUN sudo apt install -y libgl1-mesa-glx

# 安裝 requirements.txt 中所列的必要套件
RUN pip install -r requirements.txt

# 讓 連接埠可以從 Docker 容器外部存取
# 對 HEROKU 無效
# EXPOSE 5000

# 當 Docker 容器啟動時，執行...
# CMD ["python", "main.py"]

ENTRYPOINT ["python3"]
CMD ["main.py"]


# 20201125 原來上Heroku只能用'web'，不然他認不得 :(
# heroku container:push web