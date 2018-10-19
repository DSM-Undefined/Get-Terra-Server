from flasgger import swag_from
from flask import jsonify

from view.base_resource import BaseResource
from docs.map import RANK_MAP_GET
from model.Team import TeamModel


class Rank(BaseResource):

    @swag_from(RANK_MAP_GET)
    def get(self):
        map_: list = {'map': [[team.teamId, len(team.ownBooth)] for team in TeamModel.objects() if team.teamId != -1]}
        map_.sort(key=lambda a: a[1], reverse=True)
        return jsonify(map_)
