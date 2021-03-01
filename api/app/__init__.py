# ~/api/app/app.py

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.database.db import initialize_db
from flask_restful import Api
from app.resources.routes import initialize_routes

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)
