from flasgger import swag_from

from view.base_resource import BaseResource
from docs.account import SIGNUP_POST


class Signup(BaseResource):

    @swag_from(SIGNUP_POST)
    def post(self):
        pass
