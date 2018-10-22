from flasgger import swag_from
from flask import jsonify

from view.base_resource import BaseResource
from docs.map import RANK_MAP_GET
from model.Team import TeamModel
from model.Booth import BoothModel


class Rank(BaseResource):

    @swag_from(RANK_MAP_GET)
    def get(self):
        teams = [[team.teamId, len(BoothModel.objects(ownTeam=team))] for team in TeamModel.objects() if team.teamId != -1]
        teams.sort(key=lambda a: a[1], reverse=True)

        map_ = {'map': {}}
        for i in range(len(teams)):
            map_['map'][str(i+1)] = {'team': teams[i][0], 'booths': teams[i][1]}

        return jsonify(map_)
