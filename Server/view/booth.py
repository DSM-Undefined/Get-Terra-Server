from flask import request, Response, current_app, abort
from flasgger import swag_from


from docs.booth import *
from model.Booth import BoothModel
from model.Team import TeamModel
from view.base_resource import BaseResource


class Booth(BaseResource):

    @swag_from(BOOTH_PUT)
    def put(self):
        payload = request.json
        if payload['secretKey'] != current_app.config['SECRET_KEY']:
            abort(403)

        boothNameList = request.json['boothNameList']
        if not boothNameList:
            return Response('', 205)

        default_team = TeamModel.objects(teamName='empty').first()
        booths = [booth.boothName for booth in BoothModel.objects()]
        for booth in boothNameList:
            if booth not in booths:
                BoothModel(boothName=booth, ownTeam=default_team).save()

        return Response('', 201)

    @swag_from(BOOTH_DELETE)
    def delete(self):
        payload = request.json
        if payload['secretKey'] != current_app.config['SECRET_KEY']:
            abort(403)

        boothName = request.json['boothName']

        booth: BoothModel = BoothModel.objects(boothName=boothName).first()
        if not booth:
            return Response('', 204)

        booth.delete()
        return Response('', 201)
