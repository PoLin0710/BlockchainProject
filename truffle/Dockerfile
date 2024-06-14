# 基於 Node.js 官方映像建立
FROM node:14

# 設置工作目錄
WORKDIR /usr/src/app

# 安裝 Truffle 和 Ganache CLI
RUN npm install -g truffle@5.4.29 ganache-cli

# 複製 package.json 和 package-lock.json 以安裝 npm 依賴
COPY package*.json ./

# 安裝 npm 依賴
RUN npm install

# 複製所有項目文件到工作目錄
COPY . .

# 暴露端口 8545 給 Ganache 使用
EXPOSE 8545

# 設置 Docker 容器啟動時的命令
CMD ["truffle", "migrate", "--network", "development"]
