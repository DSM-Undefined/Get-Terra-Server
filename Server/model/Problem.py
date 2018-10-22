from mongoengine import *


class ProblemModel(Document):
    """
    출제되는 문제에 관한 상위 Collection
    """
    meta = {
        'collection': 'problem'
    }

    problemId = IntField(
        primary_key=True
    )

    problemType = IntField(
        required=True
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