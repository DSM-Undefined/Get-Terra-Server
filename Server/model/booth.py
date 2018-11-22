from mongoengine import *
from datetime import datetime

from model.game import GameModel
from model.team import TeamModel


class BoothModel(Document):
    """
    부스에 관한 정보가 담겨있는 Collection
    """
    meta = {
        "collection": "booth"
    }

    game: GameModel = ReferenceField(
        document_type=GameModel,
        required=True,
        reverse_delete_rule=CASCADE
    )
    
    booth_name = StringField(
        primary_key=True,
        required=True
    )

    own_team: TeamModel = ReferenceField(
        document_type=TeamModel,
        required=True
    )

    next_capture_time = DateTimeField(
        default=datetime(2001, 4, 20)
    )
