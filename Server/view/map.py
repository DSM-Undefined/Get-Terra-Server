from typing import List

from flask_restful import Resource
from flasgger import swag_from
from flask import jsonify, abort, g, Response
from flask_jwt_extended import jwt_required

from docs.map import MAP_GET
from model.booth import BoothModel
from model.team import TeamModel
from util import set_g_object


class MapView(Resource):

    @swag_from(MAP_GET)
    @jwt_required
    @set_g_object
    def get(self) -> Response:
        if not g.user:
            return abort(403)

        default_team: TeamModel = TeamModel.objects(team_id=0, game=g.game).first()
        map_: dict = {'map': {}, 'myTeam': g.user.team.team_id, 'myTeamColor': g.user.team.team_color}
        booths: List[BoothModel] = BoothModel.objects(game=g.game)

        for booth in booths:
            if booth.own_team == default_team:
                map_['map'][booth.booth_name] = -1
            elif booth.own_team == g.user.team:
                map_['map'][booth.booth_name] = 1
            else:
                map_['map'][booth.booth_name] = 0

        return jsonify(map_)
