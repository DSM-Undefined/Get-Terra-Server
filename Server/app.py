from flask import Flask
from flasgger import Swagger

from config import Config
from view import Router


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    Router(app).register()

    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    return app
