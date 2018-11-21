from flask_restful import Resource
from flasgger import swag_from
from flask import Response, jsonify, abort, request, g
from flask_jwt_extended import jwt_required, get_jwt_identity

from datetime import datetime, timedelta
from random import choice

from docs.solve import SOLVE_GET, SOLVE_POST
from model.user import UserModel
from model.game import GameModel
from model.problem import ProblemModel
from model.booth import BoothModel
from util import set_g_object


class SolveView(Resource):

    def _check_time(self, game: GameModel):
        now = datetime.now()
        if now < game.start_time:
            abort(406)
        if game.end_time <= now:
            abort(412)

    @swag_from(SOLVE_GET)
    @jwt_required
    @set_g_object
    def get(self, boothName: str):

        self._check_time(g.game)

        booth: BoothModel = BoothModel.objects(booth_name=boothName).first()
        if not booth:
            return Response('', 204)

        if booth.own_team == g.user.team:
            return Response('', 205)

        if booth.next_capture_time > datetime.now():
            abort(408)

        problem: ProblemModel = choice(ProblemModel.objects())

        response = {'boothName': boothName,
                    'problemId': problem.problem_id,
                    'content': problem.content,
                    'choices': problem.choices}

        return jsonify(response)

    @swag_from(SOLVE_POST)
    @jwt_required
    @set_g_object
    def post(self, boothName: str):

        self._check_time(g.game)

        payload: dict = request.json

        problem: ProblemModel = ProblemModel.objects(problem_id=payload['problemId']).first()
        booth: BoothModel = BoothModel.objects(booth_name=boothName).first()
        if not all((problem, booth)):
            return Response('', 204)

        if booth.next_capture_time > datetime.now():
            abort(408)

        if payload['answer'] != problem.answer:
            return Response('', 205)

        booth.own_team = g.user.team
        booth.next_capture_time = datetime.now() + timedelta(minutes=1)
        booth.save()

        return Response('', 201)
