from mongoengine import *


class Club(Document):
    """
    동아리에 관한 정보가 담겨있는 Collection
    """
    meta = {
        "collection": "Club"
    }

    clubID = StringField(
        primary_key=True
    )

    clubName = StringField(
        required=True
    )

    ownTeam = IntField(
        required=True
    )