from web3 import Web3
from config import Config

web3 = Web3(Web3.HTTPProvider(Config.GANACHE_URL))

class ContractFunctionsForInfo:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(Config.GANACHE_URL))
        self.contract_address = Web3.to_checksum_address(Config.CONTRACT_INFO_ADDRESS)
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=Config.CONTRACT_INFO_ABI)


    def get_info(self, user_address):
        return self.contract.functions.getInfo().call({'from': user_address})

    def get_links(self, user_address):
        return self.contract.functions.getLinks().call({'from': user_address})