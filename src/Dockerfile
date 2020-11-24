# 使用官方的拍粉執行環境作為基本的 Docker Image
FROM python:3.9-slim

# 設定工作目錄為 /app
WORKDIR /app

# 複製目前目錄下的內容，放進 Docker 中的 /app
ADD . /app

# 安裝 requirements.txt 中所列的必要套件
RUN pip install -r requirements.txt

# 讓 連接埠可以從 Docker 容器外部存取
EXPOSE 5000

# 定義環境變數
# ENV NAME World

# RUN file="$(ls)" && echo $file


# 當 Docker 容器啟動時，執行...
CMD ["python", "main.py"]