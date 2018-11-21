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

    team_id = IntField(
        required=True
    )

    team_color = StringField(
        required=True
    )
