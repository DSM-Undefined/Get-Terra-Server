from mongoengine import *


class UserInfo(Document):
    """
    사용자 정보 관련 Collection
    """
    meta = {
        "collection": "UserInfo"
    }

    userID = StringField(
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
