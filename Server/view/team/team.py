from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, jsonify, Response, request

from view.base_resource import BaseResource
from docs.team import TEAM_GET, TEAM_POST
from model.user import UserModel
from model.team import TeamModel


class Team(BaseResource):

    @swag_from(TEAM_GET)
    @jwt_required
    def get(self):
        user = UserModel.objects(userId=get_jwt_identity()).first()
        if not user:
            abort(403)

        result = {team.teamNam: [user.userId for user in UserModel.objects(team=team)] for team in TeamModel.objects()}
        return jsonify(result)

    @swag_from(TEAM_POST)
    @jwt_required
    def post(self):
        user: UserModel = UserModel.objects(userId=get_jwt_identity()).first()
        if not user:
            abort(403)

        if user.team.teamName != 'empty':
            return Response('', 204)

        team: TeamModel = TeamModel.objects(teamName=int(request.args.get('team'))).first()
        if (not team) or len(UserModel.objects(team=team)) > 5:
            return Response('', 205)

        user.team = team
        user.save()

        return Response('', 201)
