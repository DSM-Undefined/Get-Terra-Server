from mongoengine import *
from datetime import datetime

from model.game import GameModel


class BoothModel(Document):
    """
    부스에 관한 정보가 담겨있는 Collection
    """
    meta = {
        "collection": "booth"
    }

    game = ReferenceField(
        document_type=GameModel,
        required=True,
        reverse_delete_rule=CASCADE
    )
    
    boothName = StringField(
        primary_key=True,
        required=True
    )

    ownTeam = ReferenceField(
        document_type='TeamModel',
        required=True
    )

    nextCaptureTime = DateTimeField(
        default=datetime(2001, 4, 20)
    )
