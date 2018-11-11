from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from flask_jwt_extended import JWTManager

from mongoengine import connect

from config import Config
from view import Router
from util import add_claims


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    Router(app).register()
    CORS(app)

    jwt = JWTManager(app)
    jwt.user_claims_loader(add_claims)

    connect('get-terra')

    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    return app
