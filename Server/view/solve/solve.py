from flasgger import swag_from
from flask import Response, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from datetime import datetime, timedelta
from random import choice
import os

from view.base_resource import BaseResource
from docs.solve import SOLVE_GET, SOLVE_POST, SOLVE_PUT
from model.user import UserModel
from model.problem import ProblemModel
from model.booth import BoothModel


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

        problem: ProblemModel = choice(ProblemModel.objects())

        response = {'boothName': boothName,
                    'problemId': problem.problemId,
                    'content': problem.content,
                    'choices': problem.choices}

        return jsonify(response)

    @swag_from(SOLVE_POST)
    @jwt_required
    def post(self, boothName: str):
        user: UserModel = UserModel.objects(userId=get_jwt_identity()).first()
        if not user:
            return abort(403)
        payload: dict = request.json

        problem: ProblemModel = ProblemModel.objects(problemId=payload['problemId']).first()
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

    @swag_from(SOLVE_PUT)
    def put(self, boothName):
        payload = request.json
        if payload['secretKey'] != os.getenv('SECRET_KEY'):
            abort(403)

        for a in payload['problems']:
            ProblemModel(**a).save()
        return Response('', 201)
