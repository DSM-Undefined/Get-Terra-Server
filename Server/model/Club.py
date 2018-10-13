from mongoengine import *


class Club(Document):
    """
    동아리에 관한 정보가 담겨있는 Collection
    """
    meta = {
        "collection": "club"
    }

    clubId = StringField(
        primary_key=True
    )

    clubName = StringField(
        required=True
    )

    ownTeam = IntField(
        required=True
    )
    # 현재 이 동아리 지역을 점령하고 있는 팀의 id
