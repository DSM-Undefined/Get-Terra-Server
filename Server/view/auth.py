from flask_restful import Resource
from flasgger import swag_from
from flask import request, jsonify, abort
from flask_jwt_extended import create_access_token

from datetime import timedelta
from werkzeug.security import check_password_hash, generate_password_hash

from model.user import UserModel
from docs.account import AUTH_POST, CHECK_GAME_KEY_GET


class AuthView(Resource):

    def encrypt_password(self, pw):
        return generate_password_hash(pw)

    @swag_from(CHECK_GAME_KEY_GET)
    def get(self):
        pass

    @swag_from(AUTH_POST)
    def post(self):
        payload = request.json

        user: UserModel = UserModel.objects(userId=payload['id']).first()
        if check_password_hash(user.password, payload['password']):
            return jsonify({"accessTocken": create_access_token(identity=user.userId, expires_delta=timedelta(days=1))})

        abort(401)
