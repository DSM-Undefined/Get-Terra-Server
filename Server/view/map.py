from flask_restful import Resource
from flasgger import swag_from
from flask import jsonify, abort, g
from flask_jwt_extended import jwt_required

from docs.map import MAP_GET
from model.booth import BoothModel
from model.team import TeamModel
from util import set_g_object


class MapView(Resource):

    @swag_from(MAP_GET)
    @jwt_required
    @set_g_object
    def get(self):
        if not g.user:
            return abort(403)

        default_team: TeamModel = TeamModel.objects(teamId=0, game=g.game).first()
        map_ = {'map': {}, 'myTeam': g.user.team.teamId, 'myTeamColor': g.user.team.teamColor}
        for booth in BoothModel.objects(game=g.game):
            if booth.ownTeam == default_team:
                map_['map'][booth.boothName] = -1
            elif booth.ownTeam == g.user.team:
                map_['map'][booth.boothName] = 1
            else:
                map_['map'][booth.boothName] = 0

        return jsonify(map_)
