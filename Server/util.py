from functools import wraps

from flask import abort, g
from flask_jwt_extended import get_jwt_claims

from model.user import UserModel
from model.game import GameModel


def add_claims(user_id):
    return {
        'user_id': user_id,
        'game_key': UserModel.objects(userId=user_id).first().game.gameKey
    }


def set_g_object(fn):
    @wraps(fn)
    def wrapper(*arg, **kwargs):
        jwt = get_jwt_claims()
        g.user = UserModel.objects(userId=jwt['user_id']).first()
        g.game = GameModel.objects(gameKey=jwt['game_key']).first()
        return fn(*arg, **kwargs)
    return wrapper