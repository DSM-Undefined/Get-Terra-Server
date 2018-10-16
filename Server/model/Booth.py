from mongoengine import *


class BoothModel(Document):
    """
    동아리에 관한 정보가 담겨있는 Collection
    """
    meta = {
        "collection": "booth"
    }

    boothId = StringField(
        primary_key=True
    )

    boothName = StringField(
        required=True
    )

    ownTeam = IntField(
        required=True
    )
    # 현재 이 동아리 지역을 점령하고 있는 팀의 id
    # -1는 점령되지 않은 지역을 뜻함
