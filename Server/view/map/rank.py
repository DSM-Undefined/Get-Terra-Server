from flasgger import swag_from

from view.base_resource import BaseResource
from docs.map import RANK_MAP_GET


class Rank(BaseResource):

    @swag_from(RANK_MAP_GET)
    def get(self):
        pass
