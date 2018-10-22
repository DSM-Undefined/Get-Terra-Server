from mongoengine import *


class TeamModel(Document):
    meta = {
        'collection': 'team'
    }

    teamName = StringField(
        primary_key=True
    )
