from flasgger import swag_from
from flask import jsonify

from view.base_resource import BaseResource
from docs.map import RANK_MAP_GET
from model.Team import TeamModel


class Rank(BaseResource):

    @swag_from(RANK_MAP_GET)
    def get(self):
        map_ = {'map': [[team.teamId, len(team.ownBooth)] for team in TeamModel.objects()]}

        return jsonify(map_)
