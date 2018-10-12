from flasgger import swag_from

from view.base_resource import BaseResource
from docs.solve import SOLVE_GET, SOLVE_POST


class Solve(BaseResource):

    @swag_from(SOLVE_GET)
    def get(self, clubId):
        pass

    @swag_from(SOLVE_POST)
    def post(self, clubId):
        pass
