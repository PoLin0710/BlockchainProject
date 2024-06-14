from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
