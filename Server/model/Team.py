from mongoengine import *
from model.User import UserModel
from model.Booth import BoothModel


class TeamModel(Document):
    teamId = IntField(
        primary_key=True,
        min_value=-1,
        max_value=4
    )

    member = ListField(
        field=UserModel,
        default=[]
    )

    ownBooth = ListField(
        field=BoothModel,
        default=[]
    )