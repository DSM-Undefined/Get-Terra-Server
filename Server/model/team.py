from mongoengine import *

from model.game import GameModel


class TeamModel(Document):
    meta = {
        'collection': 'team'
    }

    game = ReferenceField(
        document_type=GameModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    teamId = IntField(
        required=True
    )

    teamColor = StringField(
        required=True
    )
