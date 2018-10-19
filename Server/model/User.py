from mongoengine import *


class UserBase(Document):

    meta = {
        'allow_inheritance': True
    }

    userId = StringField(
        primary_key=True
    )

    email = StringField(
        required=True
    )


class UserModel(UserBase):
    """
    사용자 정보 관련 Collection
    """

    meta = {
        'collection': 'user'
    }

    password = StringField(
        required=True
    )

    team = ReferenceField(
        document_type='TeamModel',
        required=True
    )


class DeadUserModel(Document):
    meta = {
        'collection': 'dead_user'
    }
