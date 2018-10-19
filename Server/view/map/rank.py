from flasgger import swag_from
from flask import jsonify

from view.base_resource import BaseResource
from docs.map import RANK_MAP_GET
from model.Team import TeamModel
from model.Booth import BoothModel


class Rank(BaseResource):

    @swag_from(RANK_MAP_GET)
    def get(self):
        map_ = {'map': [[team.teamId, len(BoothModel.objects(ownTeam=team))] for team in TeamModel.objects() if team.teamId != -1]}
        map_['map'].sort(key=lambda a: a[1], reverse=True)
        return jsonify(map_)
