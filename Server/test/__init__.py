from pymongo import MongoClient
from unittest import TestCase as TC

from app import create_app


class TestBase(TC):

    def __init__(self):
        super(TestBase, self).__init__()

        self.client = create_app().test_client()

        self.db_name = 'get_terra_test'
        self.mongo_client = MongoClient()
        self.db = self.mongo_client[self.db_name]

    def tearDown(self):
        self.mongo_client.drop_database(self.db_name)
