from flasgger import swag_from
from flask import jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

from view.base_resource import BaseResource
from docs.map import WEB_MAP_GET, ANDROID_MAP_GET
from model.Booth import BoothModel
from model.User import UserModel


class WebMap(BaseResource):

    @swag_from(WEB_MAP_GET)
    def get(self):
        map_ = [
            [booth.boothName, booth.ownTeam] for booth in BoothModel.objects()
        ]

        return jsonify(map_), 200


class AndroidMap(BaseResource):

    @swag_from(ANDROID_MAP_GET)
    @jwt_required
    def get(self):
        user: UserModel = UserModel.objects(userId=get_jwt_identity())
        if not user:
            return Response('', 403)

        map_ = []
        for booth in BoothModel.objects():
            if booth == -1:
                map_.append([booth.boothName, None])
            elif booth == user.team:
                map_.append([booth.boothName, True])
            else:
                map_.append([booth.boothName, False])

        return jsonify(map_), 200
