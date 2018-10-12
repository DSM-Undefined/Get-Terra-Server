from flasgger import swag_from

from view.base_resource import BaseResource
from docs.team import TEAM_GET, TEAM_POST


class Team(BaseResource):

    @swag_from(TEAM_GET)
    def get(self):
        pass

    @swag_from(TEAM_POST)
    def post(self):
        pass
