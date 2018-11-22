from mongoengine import *

from model.game import GameModel
from model.team import TeamModel


class UserModel(Document):
    """
    사용자 정보 관련 Collection
    """

    meta = {
        'collection': 'user'
    }

    game: GameModel = ReferenceField(
        document_type=GameModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    user_id = StringField(
        required=True
    )

    email = StringField(
        required=True
    )

    password = StringField(
        required=True
    )

    team: TeamModel = ReferenceField(
        document_type=TeamModel,
        required=True
    )
