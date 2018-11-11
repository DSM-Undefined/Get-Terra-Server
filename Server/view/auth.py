from flask_restful import Resource
from flasgger import swag_from
from flask import request, jsonify, abort
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash

from docs.account import AUTH_POST, CHECK_GAME_KEY_GET
from model.user import UserModel
from model.game import GameModel
from util import check_gameKey


class AuthView(Resource):

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
        user: UserModel = UserModel.objects(userId=payload['id'], gameKey=gameKey).first()

        if user:
            if check_password_hash(user.password, payload['password']):
                return create_access_token(user.id)
            else:
                abort(205)

        UserModel(payload['id'], generate_password_hash(payload['password']), gameKey).save()
        return jsonify({'accessToken': create_access_token(user.id)})
