from mongoengine import *


class TeamModel(Document):
    meta = {
        'collection': 'team'
    }
    teamId = IntField(
        primary_key=True,
        min_value=-1,
        max_value=4
    )
