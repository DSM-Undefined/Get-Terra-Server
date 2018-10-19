from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, jsonify, Response, request

from view.base_resource import BaseResource
from docs.team import TEAM_GET, TEAM_POST
from model.User import UserModel
from model.Team import TeamModel


class Team(BaseResource):

    @swag_from(TEAM_GET)
    @jwt_required
    def get(self):
        user = UserModel.objects(userId=get_jwt_identity()).first()
        if not user:
            abort(403)

        result = [user.userId for team in TeamModel.objects() for user in UserModel.objects(team=team) if team.teamId != -1]
        return jsonify(result)

    @swag_from(TEAM_POST)
    @jwt_required
    def post(self):
        user: UserModel = UserModel.objects(userId=get_jwt_identity()).first()
        if not user:
            abort(403)

        if user.team.teamId != -1:
            return Response('', 204)

        team: TeamModel = TeamModel.objects(teamId=int(request.args.get('team'))).first()
        if (not team) or len(team.member) > 5:
            return Response('', 205)

        user.team = team
        user.save()

        return Response('', 201)
