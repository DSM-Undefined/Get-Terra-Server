from mongoengine import *


class GameModel(Document):
    meta = {
        'collection': 'game'
    }

    gameKey = IntField(
        primary_key=True
    )

    start_time = DateTimeField(
        required=True
    )

    end_time = DateTimeField(
        required=True
    )

    teamCount = IntField(
        required=True,
        min_value=0,
        max_value=100
    )
