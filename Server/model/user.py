from mongoengine import *

from model.game import GameModel


class UserModel(Document):
    """
    사용자 정보 관련 Collection
    """

    meta = {
        'collection': 'user'
    }

    game = ReferenceField(
        document_type=GameModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    userId = StringField(
        primary_key=True
    )

    password = StringField(
        required=True
    )

    team = ReferenceField(
        document_type='TeamModel',
        required=True
    )
