from flasgger import swag_from

from Server.view.base_resource import BaseResource
from docs.account import AUTH_POST


class Auth(BaseResource):

    @swag_from(AUTH_POST)
    def post(self):
        pass
