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
CONTRACT_INFO_ADDRESS=<部屬合約地址>
```
#   Docker
啟動專案
docker compose up --build
第一次建造時會比較久，建造完成可以看到truffle 內會產生部屬合約地址將牠放入對應的環境變數

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
           "address": "<address>",
         }'
```
### Response:
```
{
  "message": "User registered successfully",
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
           "address": "<address>"
         }'
```
### Response:
```
{
  "message": "Login successful"
}
```

##  用戶資訊
Endpoint: /auth/status

Method: GET

### Request:
```
curl -X GET "http://localhost:5000/auth/status?address=<0xYourUserAddress>"

```
### Response:
```
{
    "User": {
        "_id": "667399b421d3a99b4ec16593",
        "address": "0x0Bef52E7a0d28C053374624815A0eA87099e56F4",
        "history": [],
        "nickname": "Alice",
        "tags": []
    }
}
```

## 獲取鏈上用戶資訊
Endpoint: /blockchain/getInfo

Method: GET

### Request
```
curl -X GET "http://localhost:5000/blockchain/getInfo?address=<address>"
```
### Response
```
{
  "kyc_Confirm": false,
  "links": [
    "https://example.com",
    "https://example.org"
  ]
}
```

##  獲取用戶鏈接
Endpoint: /blockchain/getLinks

Method: GET
### Request
```
curl -X GET "http://localhost:5000/blockchain/getLinks?address=<address>"
```

### Respond
```
{
  "links": [
    "https://example.com",
    "https://example.org"
  ]
}
```


部屬合約
Truffle 設定
在 truffle 資料夾中包含 Dockerfile 和 truffle-config.js，以及 contracts 資料夾，用於存放智能合約。
