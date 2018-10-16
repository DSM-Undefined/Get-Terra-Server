from flasgger import swag_from
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from view.base_resource import BaseResource
from docs.map import WEB_MAP_GET, ANDROID_MAP_GET
from model import UserInfo, Club


class WebMap(BaseResource):

    @swag_from(WEB_MAP_GET)
    def get(self):
        obj = [
            [club.clubName, club.ownTeam] for club in Club.objects()
        ]

        return jsonify(obj), 200


class AndroidMap(BaseResource):

    @swag_from(ANDROID_MAP_GET)
    @jwt_required
    def get(self):
        if UserInfo.objects(userId=get_jwt_identity()):
            user_team = UserInfo.objects(id=get_jwt_identity()).team
            success_200 = [
                [club.clubName, "true"] for club in Club.objects() if user_team == club.ownTeam  # 자신의 팀이 점령함
                [club.clubName, "false"] for club in Club.objects() if user_team != club.ownTeam  # 다른 팀이 점령함
                [club.clubName, "null"] for club in Club.objects() if user_team == -1  # 아직 점령되지 않음
            ]

            return jsonify(success_200), 200
        # 위 조건 충족시 map 상황(사용자 팀 기준) 전달
