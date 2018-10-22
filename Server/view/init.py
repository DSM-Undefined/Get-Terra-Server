from datetime import datetime
from flask import current_app, request, abort
from flasgger import swag_from
from json import dumps
import os

from view.base_resource import BaseResource

from model.Booth import BoothModel
from model.Team import TeamModel
from model.User import UserModel, DeadUserModel

from docs.init import INIT_GAME_POST


class InitGame(BaseResource):

    @swag_from(INIT_GAME_POST)
    def post(self):

        payload = request.json
        if payload['secretKey'] != current_app.config['SECRET_KEY']:
            abort(403)

        default_team = TeamModel.objects(teamId=-1).first()
        for booth in BoothModel.objects():
            booth.ownTeam = default_team
            booth.save()

        payload = request.json

        start = payload['start']
        end = payload['end']

        current_app.config['START_TIME'] = datetime(**start)
        current_app.config['END_TIME'] = datetime(**end)

        os.putenv('START_TIME', dumps(start))
        os.putenv('END_TIME', dumps(end))

        for user in UserModel.objects(team__ne=default_team):
            DeadUserModel(userId=user.userId, email=user.email)
