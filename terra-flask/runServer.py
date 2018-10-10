from flask import Flask
from flask_restful import Api, Resource
from refact.login import Login

app = Flask(__name__)
api = Api(app)

app.add_resource(Login, '/login')
