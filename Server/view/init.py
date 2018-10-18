from datetime import datetime
from flask import current_app, request, abort
from flasgger import swag_from

from view.base_resource import BaseResource

from model.Booth import BoothModel
from model.Team import TeamModel

from docs.init import INIT_GAME_POST


class InitGame(BaseResource):

    @swag_from(INIT_GAME_POST)
    def post(self):

        payload = request.json
        if payload['secretKey'] != current_app.config['SECRET_KEY']:
            abort(403)

        for i in range(-1, 5):
            team: TeamModel = TeamModel.objects(teamId=i).first()
            if team:
                team.member = []
                team.ownBooth = []
                team.save()
            else:
                TeamModel(teamId=i).save()

        default_team = TeamModel.objects(teamId=-1).first()
        for booth in BoothModel.objects():
            booth.ownTeam = default_team
            booth.save()

        payload = request.json
        current_app.config['START_TIME'] = datetime(**(payload['start']))
        current_app.config['END_TIME'] = datetime(**(payload['end']))
