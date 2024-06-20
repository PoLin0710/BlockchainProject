from flask import Blueprint, request, jsonify
from utils.db import mongo

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nickname = data['nickname']
    address = data['address']

    if mongo.db.users.find_one({"address": address}):
        return jsonify({"error": "This address already exists"}), 400
    
    user_data = {
        "nickname": nickname,
        "address": address,
        "tags": [],
        "history": [],
    }
    
    result = mongo.db.users.insert_one(user_data)
    user_data.pop('_id', None)
    return jsonify({"message": "User registered successfully", "data": user_data}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    address = data['address']
    
    user = mongo.db.users.find_one({"address": address})
    if user is None:
        return jsonify({"error": "Invalid address"}), 401
    
    return jsonify({"message": "Login successful"}), 200

@auth_bp.route('/status', methods=['GET'])
def status():
    current_address = request.args.get("address")
    user = mongo.db.users.find_one({"address": current_address})
    user.pop('_id', None)

    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"User":user}), 200
