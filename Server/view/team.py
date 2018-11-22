from typing import List

from flask_restful import Resource
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from flask import abort, jsonify, Response, request, g

from docs.team import TEAM_GET, TEAM_POST
from model.user import UserModel
from model.team import TeamModel

from util import set_g_object


class TeamView(Resource):

    @swag_from(TEAM_GET)
    @jwt_required
    @set_g_object
    def get(self) -> Response:
        team_objects: List[TeamModel] = TeamModel.objects(game=g.game)
        result = {'teamCount': len(team_objects)}

        for team in team_objects:
            result[str(team.team_id)] = {
                'member': [user.user_id for user in UserModel.objects(team=team)],
                'teamColor': team.team_color
            }

        return jsonify(result)

    @swag_from(TEAM_POST)
    @jwt_required
    @set_g_object
    def post(self) -> Response:
        if not g.user:
            abort(403)

        if g.user.team.team_id != 0:
            return Response('', 204)

        team: TeamModel = TeamModel.objects(team_id=int(request.args.get('team'))).first()
        if (not team) or len(UserModel.objects(team=team)) > 5:
            return Response('', 205)

        g.user.team = team
        g.user.save()

        return Response('', 201)
