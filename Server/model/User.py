from mongoengine import *


class UserModel(Document):
    """
    사용자 정보 관련 Collection
    """

    meta = {
        'collection': 'user'
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

    team = ReferenceField(
        document_type='TeamModel',
        required=True
    )
