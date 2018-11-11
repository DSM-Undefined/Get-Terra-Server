from flask_restful import Resource
from flasgger import swag_from
from flask import jsonify, Response, abort, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

from datetime import datetime

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
                map_['map'][booth.boothName] = None
            elif booth.ownTeam == g.user.team:
                map_['map'][booth.boothName] = True
            else:
                map_['map'][booth.boothName] = False

        return jsonify(map_)
