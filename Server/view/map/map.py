from flasgger import swag_from
from flask import jsonify, Response, abort, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

from datetime import datetime

from view.base_resource import BaseResource
from docs.map import WEB_MAP_GET, ANDROID_MAP_GET

from model.Booth import BoothModel
from model.User import UserModel
from model.Team import TeamModel


class WebMap(BaseResource):

    @swag_from(WEB_MAP_GET)
    def get(self):
        end: datetime = current_app.config['END_TIME']
        end = {'year': end.year, 'month': end.month, 'day': end.day, 'hour': end.hour, 'minute': end.minute}
        map_ = {
            'map': [[booth.boothName, booth.ownTeam.teamId] for booth in BoothModel.objects()],
            'endTime': end
        }

        return jsonify(map_)


class AndroidMap(BaseResource):

    @swag_from(ANDROID_MAP_GET)
    @jwt_required
    def get(self):
        user: UserModel = UserModel.objects(userId=get_jwt_identity()).first()
        if not user:
            return abort(403)

        default_team: TeamModel = TeamModel.objects(teamId=-1).first()
        end: datetime = current_app.config['END_TIME']
        end = {'year': end.year, 'month': end.month, 'day': end.day, 'hour': end.hour, 'minute': end.minute}
        map_ = {'map': [], 'endTime': end, 'myTeam': user.team.teamId}
        for booth in BoothModel.objects():
            if booth.ownTeam == default_team:
                map_['map'].append([booth.boothName, None])
            elif booth == user.team:
                map_['map'].append([booth.boothName, True])
            else:
                map_['map'].append([booth.boothName, False])

        return jsonify(map_)
