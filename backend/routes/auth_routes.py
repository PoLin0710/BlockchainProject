from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from utils.db import mongo, bcrypt
from utils.blockchain import create_blockchain_account ,ContractFunctions

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nickname = data['nickname']
    username = data['username']
    password = data['password']
    
    if mongo.db.users.find_one({"username": username}):
        return jsonify({"error": "Username already exists"}), 400
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    account = create_blockchain_account()
    
    user_data = {
        "nickname": nickname,
        "username": username,
        "password": hashed_password,
        "address": account['address'],
        "private_key": account['private_key'],
        "KYC Certification": False
    }
    
    mongo.db.users.insert_one(user_data)
    return jsonify({"message": "User registered successfully", "address": account['address']}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    user = mongo.db.users.find_one({"username": username})
    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify({"message": "Login successful", "access_token": access_token, "address": user['address']}), 200
    
    return jsonify({"error": "Invalid username or password"}), 401

@auth_bp.route('/kycConfirm',methods=['POST'])
@jwt_required()
def kycConfirm():
    current_user = get_jwt_identity()
    result = mongo.db.users.find_one_and_update(
        {"username": current_user},
        {"$set": {"KYC Certification": True}},
        return_document=True
    )
    if result:
        return jsonify({"message": "KYC Confirmed"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

@auth_bp.route('/status', methods=['GET'])
@jwt_required()
def status():
    current_user = get_jwt_identity()
    user = mongo.db.users.find_one({"username": current_user})
    if not user:
        return jsonify({"error": "User not found"}), 404

    nickname = user.get("nickname")
    username = user.get("username")
    address = user.get("address")
    
    if not address:
        return jsonify({"error": "User address not found"}), 404

    # 獲取用戶的信譽積分
    points = ContractFunctions().get_credit_points(address)

    return jsonify({
        "nickname": nickname,
        "username": username,
        "credit_points": points
    }), 200
