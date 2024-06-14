from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.db import mongo
from utils.blockchain import web3,ContractFunctions

blockchain_bp = Blueprint('blockchain', __name__)

@blockchain_bp.route('/balance', methods=['GET'])
@jwt_required()
def get_balance():
    username = get_jwt_identity()
    
    user = mongo.db.users.find_one({"username": username})
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    address = user['address']
    balance = web3.eth.get_balance(address)
    balance_eth = web3.from_wei(balance, 'ether')
    
    return jsonify({"address": address, "balance": balance_eth}), 200

@blockchain_bp.route('/check_connection', methods=['GET'])
def check_connection():
    if web3.is_connected():
        return jsonify({"status": "connected", "blockNumber": web3.eth.block_number,"blockHash":web3.eth.get_block('latest')['hash'].hex(),"NetID":web3.eth.chain_id})
    else:
        return jsonify({"status": "not connected"}), 500
    
contract_functions = ContractFunctions()

@blockchain_bp.route('/vote', methods=['POST'])
@jwt_required()
def vote():
    current_user = get_jwt_identity()
    user = mongo.db.users.find_one({'username': current_user})
    if not user:
        return jsonify({'msg': 'User not found'}), 404
    
    from_address = user.get('address')
    if not from_address:
        return jsonify({'msg': 'User address not found'}), 404

    to_username = request.json['to']
    to_user = mongo.db.users.find_one({'username': to_username})
    if not to_user:
        return jsonify({'msg': 'Recipient user not found'}), 404
    
    to_address = to_user.get('address')
    if not to_address:
        return jsonify({'msg': 'Recipient address not found'}), 404
    
    like = request.json['like']
    tx_hash = contract_functions.vote(to_address, from_address, like)
    return jsonify({'tx_hash': tx_hash})

@blockchain_bp.route('/credit_points', methods=['GET'])
@jwt_required()
def get_credit_points():
    current_user = get_jwt_identity()
    user = mongo.db.users.find_one({'username': current_user})
    if not user:
        return jsonify({'msg': 'User not found'}), 404
    
    address = user.get('address')
    if not address:
        return jsonify({'msg': 'User address not found'}), 404
    
    points = contract_functions.get_credit_points(address)
    return jsonify({'credit_points': points})

#Test
@blockchain_bp.route('/create_info', methods=['POST'])
@jwt_required()
def create_info():
    current_user = get_jwt_identity()
    user = mongo.db.users.find_one({'username': current_user})
    if not user:
        return jsonify({'msg': 'User not found'}), 404
    
    user_address = user.get('address')
    if not user_address:
        return jsonify({'msg': 'User address not found'}), 404
    
    tx_hash = contract_functions.create_info(user_address)
    return jsonify({'tx_hash': tx_hash})