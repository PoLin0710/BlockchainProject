from flask import Flask
from config import Config
from routes.auth_routes import auth_bp
from routes.blockchain_routes import blockchain_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

# 初始化 JWT
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(blockchain_bp, url_prefix='/blockchain')

if __name__ == '__main__':
    app.run(debug=True)
