from web3 import Web3
from config import Config

web3 = Web3(Web3.HTTPProvider(Config.GANACHE_URL))

# 智能合約的 ABI 和地址 要改
contract_address = Config.CONTRACT_INFO_ADDRESS
contract_abi = [
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "creditPoints",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": True
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "isCreate",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": True
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "user",
          "type": "address"
        }
      ],
      "name": "createInfo",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "like",
          "type": "bool"
        }
      ],
      "name": "vote",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

class ContractFunctions:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(Config.GANACHE_URL))
        self.contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)

    def create_info(self, user_address):
        tx = self.contract.functions.createInfo(user_address).build_transaction({
            'from': Config.ACCOUNT_ADDRESS,
            'nonce': self.w3.eth.get_transaction_count(Config.ACCOUNT_ADDRESS),
            'gas': 2000000,
            'gasPrice': self.w3.to_wei('50', 'gwei')
        })
        signed_tx = self.w3.eth.account.sign_transaction(tx, Config.PLATFORM_PRIVATE_KEY)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def vote(self, to_address, from_address, like):
        tx = self.contract.functions.vote(to_address, from_address, like).build_transaction({
            'from': Config.ACCOUNT_ADDRESS,
            'nonce': self.w3.eth.get_transaction_count(Config.ACCOUNT_ADDRESS),
            'gas': 2000000,
            'gasPrice': self.w3.to_wei('50', 'gwei')
        })
        signed_tx = self.w3.eth.account.sign_transaction(tx, Config.PLATFORM_PRIVATE_KEY)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def get_credit_points(self, address):
        points = self.contract.functions.creditPoints(address).call()
        return points

def create_blockchain_account():
    account = web3.eth.account.create()
    ContractFunctions().create_info(account.address)
    return {
        'address': account.address,
        'private_key': account._private_key.hex()
    }