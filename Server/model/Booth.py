from mongoengine import *
from model.Team import TeamModel


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

    ownTeam = ReferenceField(
        document_type=TeamModel,
        required=True
    )
