from mongoengine import *


class UserModel(Document):
    """
    사용자 정보 관련 Collection
    """

    meta = {
        'collection': 'user-info'
    }

    userId = StringField(
        primary_key=True
    )

    email = StringField(
        required=True
    )

    password = StringField(
        required=True
    )

    team = IntField(
        required=True
    )