from unittest import TestCase as TC
from app import create_app


class TestBase(TC):

    def __init__(self):
        super(TestBase, self).__init__()

        self.client = create_app().test_client()
