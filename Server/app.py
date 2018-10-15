from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager

from config import Config
from view import Router


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    Router(app).register()
    jwt = JWTManager(app)

    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    return app
