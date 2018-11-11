from flask import abort

from model.game import GameModel


def check_gameKey(fn):
    def wrapper(gameKey):
        if not GameModel.objects(gameKey=gameKey).first():
            abort(204)
            return fn(gameKey)
    return wrapper


def add_claims(user_id):
    return {
        'user_id': user_id,
        'game_key': GameModel.objects(user_id).first()['gameKey']
    }
