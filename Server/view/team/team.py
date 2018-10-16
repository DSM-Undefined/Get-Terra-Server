from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, jsonify, Response, request

from view.base_resource import BaseResource
from docs.team import TEAM_GET, TEAM_POST
from model.UserInfo import UserInfo
from model.Team import TeamModel


class Team(BaseResource):

    @swag_from(TEAM_GET)
    @jwt_required
    def get(self):
        user = UserInfo.objects(userId=get_jwt_identity()).first()
        if not user:
            abort(403)

        team = [[], [], [], []]
        for user in UserInfo.objects():
            if user.team != -1:
                team[user.team].append(user.userId)

        return jsonify(team)

    @swag_from(TEAM_POST)
    @jwt_required
    def post(self):
        user: UserInfo = UserInfo.objects(userId=get_jwt_identity()).first()
        if not user:
            abort(403)

        if user.team.teamId != -1:
            return Response('', 204)

        team: TeamModel = TeamModel.objects(teamId=int(request.args.get('team'))).first()
        if not team or len(team.member) > 5:
            return Response('', 205)

        user.team = team
        team.member.append(user)

        user.save()
        team.save()

        return Response('', 201)
