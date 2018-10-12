from flask import Flask

from .config import Config
from .view import Router


def create_app():
    app = Flask(__name__)

    app.config_class(Config)
    Router(app).register_blueprint()

    return app
