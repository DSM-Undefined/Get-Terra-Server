from datetime import datetime, timedelta
from functools import wraps
from json import dumps, loads

from mongoengine.connection import get_connection
from unittest import TestCase

from app import create_app

from model.game import GameModel
from model.team import TeamModel


class TCBase(TestCase):

    def setUp(self):
        self.client = create_app().test_client()
        self._create_game()
        self._create_team()

    def tearDown(self):
        connection = get_connection()
        connection.drop_database('get-terra')

    def _create_game(self, game_key=100000, team_count=4):
        GameModel(game_key, datetime.now(), datetime.now()+timedelta(days=1), team_count).save()

    def _create_team(self, team_count=4):
        game = GameModel.objects(gameKey=100000).first()
        for i in range(team_count+1):
            TeamModel(game, i, hex(i*333333)).save()

    def _create_access_token(self, game_key=100000, id_='test', password='test', email='test@test.com'):
        rv = self.client.post(
            '/auth/' + str(game_key),
            data=dumps(dict(id=id_, password=password, email=email)),
            content_type='application/json'
        )

        return loads(rv.data, encoding='utf-8')['accessToken']


def check_status_code(status_code):
    def decorator(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            rv = fn(self, *args, **kwargs)
            self.assertEqual(rv.status_code, status_code)
        return wrapper
    return decorator
