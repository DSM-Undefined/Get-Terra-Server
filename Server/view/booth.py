from flask import request, Response, jsonify
from flasgger import swag_from


from docs.booth import *
from model.Booth import BoothModel
from model.Team import TeamModel
from view.base_resource import BaseResource


class Booth(BaseResource):

    @swag_from(BOOTH_GET)
    def get(self):
        booths = [[booth.boothName, booth.ownTeam.teamId]for booth in BoothModel.objects()]
        if not booths:
            return Response('', 204)
        return jsonify(booths)

    @swag_from(BOOTH_POST)
    def post(self):
        boothNameList = request.json['boothNameList']
        if not boothNameList:
            return Response('', 205)

        default_team = TeamModel.objects(teamId=-1).first()
        booths = [booth.boothName for booth in BoothModel.objects()]
        for booth in boothNameList:
            if booth not in booths:
                BoothModel(boothName=booth, ownTeam=default_team).save()

        return Response('', 201)

    @swag_from(BOOTH_DELETE)
    def delete(self):
        boothName = request.json['boothName']

        booth: BoothModel= BoothModel.objects(boothName=boothName).first()
        if not booth:
            return Response('', 204)

        booth.delete()
        return Response('', 201)
