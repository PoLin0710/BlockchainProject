# 使用 Python 3.8 映像檔作為基礎
FROM python:3.12.1-slim

# 設定工作目錄
WORKDIR /app

# 安裝必要的系統依賴
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式源代碼
COPY . .

# 設定環境變量
ENV FLASK_APP=main.py

# 執行應用程式
CMD ["flask", "run", "--host=0.0.0.0"]
