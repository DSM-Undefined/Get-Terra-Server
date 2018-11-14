from flask_restful import Resource
from flasgger import swag_from
from flask import request, jsonify, abort, Response
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash

from docs.account import AUTH_POST, CHECK_GAME_KEY_GET
from model.user import UserModel
from model.game import GameModel
from model.team import TeamModel


class AuthView(Resource):

    @swag_from(CHECK_GAME_KEY_GET)
    def get(self, gameKey):
        if not GameModel.objects(gameKey=gameKey).first():
            return Response('', 204)
        return jsonify({'gameKey': gameKey})

    @swag_from(AUTH_POST)
    def post(self, gameKey):
        payload = request.json
        game: GameModel = GameModel.objects(gameKey=gameKey).first()
        if not game:
            return Response('', 204)

        user: UserModel = UserModel.objects(userId=payload['id'], game=game).first()
        if user:
            if check_password_hash(user.password, payload['password']):
                return create_access_token(payload['id'])
            else:
                return Response('', 205)

        default_team = TeamModel.objects(game=game, teamId=0).first()
        UserModel(game, payload['id'], payload['email'], generate_password_hash(payload['password']), default_team).save()
        return jsonify({'accessToken': create_access_token(payload['id'])})
