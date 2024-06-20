from flask import Blueprint, request, jsonify
from utils.db import mongo
from utils.blockchain import web3,ContractFunctionsForInfo

blockchain_bp = Blueprint('blockchain', __name__)

contract_functions = ContractFunctionsForInfo()

@blockchain_bp.route('/getInfo', methods=['GET'])
def get_info():
    user_address = request.args.get('address')
    if not user_address:
        return jsonify({'error': 'address is required'}), 400
    try:
        info = contract_functions.get_info(user_address)
        return jsonify({'kyc_Confirm': info[0], 'links': info[1]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@blockchain_bp.route('/getLinks', methods=['GET'])
def get_links():
    user_address = request.args.get('address')
    if not user_address:
        return jsonify({'error': 'address is required'}), 400
    try:
        links = contract_functions.get_links(user_address)
        return jsonify({'links': links})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
