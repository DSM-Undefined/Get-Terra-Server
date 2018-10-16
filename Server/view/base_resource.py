from flask_restful import Resource
from werkzeug.security import generate_password_hash


class BaseResource(Resource):

    def encrypt_password(self, pw):
        return generate_password_hash(pw)
