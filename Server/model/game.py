from mongoengine import *


class GameModel(Document):
    meta = {
        'collection': 'game'
    }

    game_key = IntField(
        primary_key=True
    )

    start_time = DateTimeField(
        required=True
    )

    end_time = DateTimeField(
        required=True
    )

    team_count = IntField(
        required=True,
        min_value=0,
        max_value=100
    )
