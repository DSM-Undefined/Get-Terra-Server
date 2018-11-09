from mongoengine import *


class GameModel(Document):
    meta = {
        'collection': 'game'
    }
