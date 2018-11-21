from datetime import datetime, timedelta
from functools import wraps
from json import dumps, loads

from mongoengine.connection import get_connection
from unittest import TestCase

from app import create_app

from model.booth import BoothModel
from model.game import GameModel
from model.team import TeamModel
from model.user import UserModel
from model.problem import ProblemModel


class TCBase(TestCase):

    def setUp(self):
        self.client = create_app().test_client()
        self.init_game()

    def tearDown(self):
        connection = get_connection()
        connection.drop_database('get-terra')

    def init_game(self):
        self.test_game = self._create_game()
        self._create_team()
        self._create_problem()
        self._create_booth()
        self.test_user, self.access_token = self._create_user_and_access_token()

    def _create_game(self, game_key=100000, team_count=4):
        test_game = GameModel(
            game_key=game_key,
            start_time=datetime.now(),
            end_time=datetime.now()+timedelta(days=1),
            team_count=team_count
        )
        test_game.save()
        return test_game

    def _create_team(self, team_count=4):
        for i in range(team_count+1):
            TeamModel(
                game=self.test_game,
                team_id=i,
                team_color=hex(i*333333)
            ).save()

    def _create_problem(self):
        ProblemModel(
            game=self.test_game,
            problem_id=1,
            content='test',
            answer='1',
            choices=['1', '2', '3', '4']
        ).save()

    def _create_booth(self):
        default_team = TeamModel.objects(team_id=0).first()
        for i in range(5):
            BoothModel(
                game=self.test_game,
                booth_name=f'booth{i}',
                own_team=default_team,
            ).save()

    def _create_user_and_access_token(self, game_key=100000, id_='test', password='test', email='test@test.com'):
        rv = self.client.post(
            '/auth/' + str(game_key),
            data=dumps(dict(id=id_, password=password, email=email)),
            content_type='application/json'
        )
        token = loads(rv.data, encoding='utf-8')['accessToken']

        test_user = UserModel.objects(game=self.test_game, user_id=id_).first()

        return test_user, f'Bearer {token}'


def check_status_code(status_code):
    def decorator(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            rv = fn(self, *args, **kwargs)
            self.assertEqual(rv.status_code, status_code)
        return wrapper
    return decorator
