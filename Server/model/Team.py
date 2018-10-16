from mongoengine import *
from model.UserInfo import UserInfo
from model.Club import Club


class TeamModel(Document):
    teamId = IntField(
        primary_key=True,
        min_value=0,
        max_value=4
    )

    member = ListField(
        field=UserInfo,
        default=[]
    )

    captured = ListField(
        field=Club,
        default=[]
    )