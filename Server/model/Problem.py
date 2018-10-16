from mongoengine import *


class ProblemBase(Document):
    """
    출제되는 문제에 관한 상위 Collection
    """
    meta = {
        'abstract': True,
        'allow_inheritance': True
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


class OXModel(ProblemBase):
    """
    OX 문항 Collection
    """
    meta = {
        'collection': 'ox_problem'
    }


class SubModel(ProblemBase):
    """
    주관식 문항 Collection
    """
    meta = {
        'collection': 'write_problem'
    }


class ChoiceModel(ProblemBase):
    """
    4지선다 Collection
    """
    meta = {
        'collection': 'choice_problem'
    }

    choices = ListField(
        StringField(
            required=True
        )
    )
