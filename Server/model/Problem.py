from mongoengine import *


class ProblemBase(Document):
    """
    출제되는 문제에 관한 상위 Collection
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
    }

    problemID = IntField(
        primary_key=True
    )

    problemType = IntField(
        required=True
    )

    content = StringField(
        required=True
    )


class OXModel(ProblemBase):
    """
    OX 문항 Collection
    """
    meta = {
        'collection': 'OXProblem'
    }

    pass


class SubModel(ProblemBase):
    """
    주관식 문항 Collection
    """
    meta = {
        'collection': 'SubProblem'
    }

    pass


class ChoiceModel(ProblemBase):
    """
    4지선다 Collection
    """
    meta = {
        'collection': 'ChoiceProblem'
    }

    choices = ListField(
        StringField(
            required=True
        )
    )
