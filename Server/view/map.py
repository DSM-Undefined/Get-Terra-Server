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

        default_team: TeamModel = TeamModel.objects(team_id=0, game=g.game).first()
        map_ = {'map': {}, 'myTeam': g.user.team.team_id, 'myTeamColor': g.user.team.team_color}
        for booth in BoothModel.objects(game=g.game):
            if booth.own_team == default_team:
                map_['map'][booth.booth_name] = -1
            elif booth.own_team == g.user.team:
                map_['map'][booth.booth_name] = 1
            else:
                map_['map'][booth.booth_name] = 0

        return jsonify(map_)
