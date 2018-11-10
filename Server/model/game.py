from mongoengine import *


class GameModel(Document):
    meta = {
        'collection': 'game'
    }

    start_time = DateTimeField(
        required=True
    )

    end_time = DateTimeField(
        required=True
    )

    teamCount = IntField(
        required=True,
        min_value=1,
        max_value=100
    )
