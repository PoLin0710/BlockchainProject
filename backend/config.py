import os
from dotenv import load_dotenv

# 加載 .env 文件中的環境變數
load_dotenv()

class Config:
    MONGO_URI = "mongodb://mongodb:27017/database"
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(24))
    PLATFORM_PRIVATE_KEY = os.getenv("PLATFORM_PRIVATE_KEY")
    GANACHE_URL = 'http://ganache:8545'
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")
    # 改部屬合約者地址
    ACCOUNT_ADDRESS = os.getenv("ACCOUNT_ADDRESS","0xC3de48388ffD3b9c30DeC08c3B2dE72D67466fD0")
    # 改部屬合約地址
    CONTRACT_INFO_ADDRESS=os.getenv("CONTRACT_INFO_ADDRESS","0x9d7fFC677AbB7f88276e83C04Fb91e9573CEcD64")
    CONTRACT_INFO_ABI=[
	{
		"inputs": [],
		"name": "getInfo",
		"outputs": [
			{
				"components": [
					{
						"internalType": "bool",
						"name": "kyc_Confirm",
						"type": "bool"
					},
					{
						"internalType": "string[]",
						"name": "links",
						"type": "string[]"
					}
				],
				"internalType": "struct UserInfo.UserData",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getLinks",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "links",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]