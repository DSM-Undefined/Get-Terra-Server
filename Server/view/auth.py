from flask_restful import Resource
from flasgger import swag_from
from flask import request, jsonify, abort
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash

from datetime import timedelta

from docs.account import AUTH_POST, CHECK_GAME_KEY_GET
from model.user import UserModel
from model.game import GameModel
from util import check_gameKey


class AuthView(Resource):

    def encrypt_password(self, pw):
        return generate_password_hash(pw)

    @check_gameKey
    @swag_from(CHECK_GAME_KEY_GET)
    def get(self, gameKey):
        if not GameModel.objects(gameKey=gameKey).first():
            abort(204)

        return jsonify({'gameKey': gameKey})

    @check_gameKey
    @swag_from(AUTH_POST)
    def post(self, gameKey):
        payload = request.json

        user: UserModel = UserModel.objects(userId=payload['id']).first()
        if check_password_hash(user.password, payload['password']):
            return jsonify({"accessTocken": create_access_token(identity=user.userId, expires_delta=timedelta(days=1))})

        abort(401)
