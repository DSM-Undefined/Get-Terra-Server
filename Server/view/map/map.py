from flasgger import swag_from
from flask import jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

from view.base_resource import BaseResource
from docs.map import WEB_MAP_GET, ANDROID_MAP_GET, RANK_MAP_GET
from model.Club import Club
from model.UserInfo import UserInfo


class WebMap(BaseResource):

    @swag_from(WEB_MAP_GET)
    def get(self):
        map_ = [
            [club.clubName, club.ownTeam] for club in Club.objects()
        ]

        return jsonify(map_), 200


class AndroidMap(BaseResource):

    @swag_from(ANDROID_MAP_GET)
    @jwt_required
    def get(self):
        user: UserInfo = UserInfo.objects(userId=get_jwt_identity())
        if not user:
            return Response('', 403)

        map_ = []
        for club in Club.objects():
            if club == -1:
                map_.append([club.clubName, None])
            elif club == user.team:
                map_.append([club.clubName, True])
            else:
                map_.append([club.clubName, False])

        return jsonify(map_), 200
