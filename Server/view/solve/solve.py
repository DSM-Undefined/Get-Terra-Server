from flasgger import swag_from
from flask import Response, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from datetime import datetime, timedelta
from random import choice

from view.base_resource import BaseResource
from docs.solve import SOLVE_GET, SOLVE_POST
from model.User import UserModel
from model.Problem import ProblemBase
from model.Booth import BoothModel


class Solve(BaseResource):

    @swag_from(SOLVE_GET)
    @jwt_required
    def get(self, boothName: str):
        user = UserModel.objects(userId=get_jwt_identity()).first()
        if not user:
            return abort(403)

        booth: BoothModel = BoothModel.objects(boothName=boothName).first()
        if not booth:
            return Response('', 204)

        if booth.ownTeam == user.team:
            return Response('', 205)

        if booth.nextCaptureTime > datetime.now():
            abort(408)

        problem: ProblemBase = choice(ProblemBase.objects())

        response = problem.to_mongo()
        response['boothName'] = boothName

        return jsonify(response)

    @swag_from(SOLVE_POST)
    @jwt_required
    def post(self, boothName: str):
        user: UserModel = UserModel.objects(userId=get_jwt_identity()).first()
        if not user:
            return abort(403)
        payload: dict = request.json

        problem: ProblemBase = ProblemBase.objects(problemId=payload['problemId']).first()
        booth: BoothModel = BoothModel.objects(boothName=boothName).first()
        if not all((problem, booth)):
            return Response('', 204)

        if booth.nextCaptureTime > datetime.now():
            abort(408)

        if payload['answer'] != problem.answer:
            return Response('', 205)

        booth.ownTeam = user.team
        booth.nextCaptureTime = datetime.now() + timedelta(minutes=1)
        booth.save()

        return Response('', 201)
