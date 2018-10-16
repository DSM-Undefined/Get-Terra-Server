from flasgger import swag_from
from flask import request, Response

from view.base_resource import BaseResource
from docs.account import SIGNUP_POST
from model.User import UserModel
from model.Team import TeamModel


class Signup(BaseResource):

    @swag_from(SIGNUP_POST)
    def post(self):
        payload = request.json

        if UserModel.objects(userId=payload['id']).first() or UserModel.objects(email=payload['email']).first():
            return Response('', 205)

        pw = self.encrypt_password(payload['password'])
        default_team = TeamModel().objects(teamId=-1)
        UserModel(userId=payload['id'], email=payload['email'], password=pw, team=default_team).save()

        return Response('', 201)
        # DB에 중복되는 닉네임이 없음을 확인하고 신규 회원 정보를 DB에 저장
        # 초기 유저 정보에는 'team'을 -1로 두어 현재 소속된 팀이 없음을 명시
