from mongoengine import *

from model.game import GameModel


class ProblemModel(Document):
    """
    출제되는 문제에 관한 상위 Collection
    """
    meta = {
        'collection': 'problem'
    }

    game = ReferenceField(
        document_type=GameModel,
        required=True,
        reverse_delete_rule=CASCADE
    )

    problem_id = IntField(
        primary_key=True
    )

    content = StringField(
        required=True
    )

    answer = StringField(
        required=True
    )

    choices = ListField(
        StringField(
            required=True
        )
    )