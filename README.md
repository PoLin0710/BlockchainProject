#   簡介(2024/06/14)
此專案使用 Flask 開發後端 API，並利用 MongoDB 作為資料庫。它提供了用戶註冊、登錄、KYC 認證、查詢餘額、投票及信用點數查詢等功能。此外，透過與智能合約的互動來執行相關功能。

#   目錄結構
```
project
│   docker-compose.yml
│   README.md
│   package-lock.json
|   package.json
|   README.md
└───node_modules
└───backend
│   │   Dockerfile
│   │   main.py
│   │   config.py
│   │   .env
|   |   requirements.txt
│   └───routes
│       │   auth_routes.py
│       │   blockchain_routes.py
│   └───utils
│       │   db.py
│       │   blockchain.py
│
└───truffle
    │   Dockerfile
    │   truffle-config.js
    │   contracts
    │       │   Info.sol
    │   migrations
    │       │   1_initial_migration.js
    │       │   2_deploy_contracts.js
    │   test
    │       │   info.test.js
```

#   環境變數 (.env)
請在專案根目錄創建 .env 文件，並設定以下變數：
```
SECRET_KEY=<你的秘密金鑰>
JWT_SECRET_KEY=<你的JWT秘密金鑰>
PLATFORM_PRIVATE_KEY=<你的平台私鑰>
ACCOUNT_ADDRESS=<ganache中的第一個地址>
CONTRACT_INFO_ADDRESS=<部屬合約地址>
```
#   Docker
啟動專案
docker compose up --build
第一次建造時會比較久，建造完成可以看到ganache 把第一個地址跟私鑰放進env

之後若只有跟改後端項目 .py檔案
docker compose up --build web

#   MongoDB 
[MongoDB 圖形化下載](https://www.mongodb.com/try/download/compass)
預設連接可以看到儲存資料

#   API 文件
##  註冊
Endpoint: /auth/register

Method: POST

### Request
```
curl -X POST http://localhost:5000/auth/register \
     -H "Content-Type: application/json" \
     -d '{
           "nickname": "<nickname>",
           "username": "<testuser>",
           "password": "<testpassword>"
         }'
```
### Response:
```
{
  "message": "User registered successfully",
  "address": "<blockchain_address>"
}
```
##  登錄
Endpoint: /auth/login

Method: POST

### Request
```
curl -X POST http://localhost:5000/auth/login \
     -H "Content-Type: application/json" \
     -d '{
           "username": "testuser",
           "password": "testpassword"
         }'
```
### Response:
```
{
  "message": "Login successful",
  "access_token": "<JWT_TOKEN>",
  "address": "<blockchain_address>"
}
```
##  KYC 認證
Endpoint: /auth/kycConfirm

Method: POST

### Headers:
```
Authorization: Bearer <JWT_TOKEN>
```
### Request:
```
curl -X POST http://localhost:5000/auth/kycConfirm \
     -H "Authorization: Bearer <JWT_TOKEN>"
```
### Response:
```
{
  "message": "KYC Confirmed"
}
```

##  用戶狀態(測試是否已經登入過) - TEST
Endpoint: /auth/status

Method: GET

### Headers:
```
Authorization: Bearer <JWT_TOKEN>
```
### Request:
```
curl -X GET http://localhost:5000/auth/status \
     -H "Authorization: Bearer <JWT_TOKEN>"
```
### Response:
```
{
  "message": "User <username> is logged in"
}
```
##  查詢餘額
Endpoint: /blockchain/balance

Method: GET

### Request:
```
curl -X GET http://localhost:5000/blockchain/balance \
     -H "Authorization: Bearer <JWT_TOKEN>"
```
### Response:
```
{
  "address": "<blockchain_address>",
  "balance": "<balance_in_eth>"
}
```
##  驗證鏈接
Endpoint: /blockchain/check_connection

Method: GET

### Request:
```
curl -X GET http://localhost:5000/blockchain/check_connection
```
### Response:
```
{
  "status": "connected",
  "blockNumber": <block_number>,
  "blockHash": "<block_hash>",
  "NetID": <network_id>
}
```
##  投票
Endpoint: /blockchain/vote

Method: POST

### Headers:
```
Authorization: Bearer <JWT_TOKEN>
```
### Request:
```
curl -X POST http://localhost:5000/blockchain/vote \
     -H "Authorization: Bearer <JWT_TOKEN>" \
     -H "Content-Type: application/json" \
     -d '{
           "to": "recipient_username",
           "like": true
         }'

```
### Response:
```
{
  "tx_hash": "<transaction_hash>"
}
```
##  查詢信用點數
Endpoint: /blockchain/credit_points

Method: GET

### Headers:
```
Authorization: Bearer <JWT_TOKEN>
```
### Request:
```
curl -X GET http://localhost:5000/blockchain/credit_points \
     -H "Authorization: Bearer <JWT_TOKEN>"
```
### Response:
```
{
  "credit_points": <points>
}
```
##  創建用戶資訊 -TEST
Endpoint: /blockchain/create_info

Method: POST

### Headers:
```
Authorization: Bearer <JWT_TOKEN>
```
### Request:
```
curl -X POST http://localhost:5000/blockchain/create_info \
     -H "Authorization: Bearer <JWT_TOKEN>"
```
### Response:
```
{
  "tx_hash": "<transaction_hash>"
}
```
部屬合約
Truffle 設定
在 truffle 資料夾中包含 Dockerfile 和 truffle-config.js，以及 contracts 資料夾，用於存放智能合約。
