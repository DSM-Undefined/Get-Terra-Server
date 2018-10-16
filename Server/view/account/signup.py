from flasgger import swag_from
from flask import request, Response

from view.base_resource import BaseResource
from docs.account import SIGNUP_POST
from model.UserInfo import UserInfo


class Signup(BaseResource):

    @swag_from(SIGNUP_POST)
    def post(self):
        payload = request.json

        if UserInfo.objects(userId=payload['id']) or UserInfo.objects(email=payload['email']):
            return Response('', 205)

        UserInfo(userId=payload['id'], email=payload['email'], password=self.encrypt_password(payload['password']), team=-1).save()

        return Response('', 201)
        # DB에 중복되는 닉네임이 없음을 확인하고 신규 회원 정보를 DB에 저장
        # 초기 유저 정보에는 'team'을 -1로 두어 현재 소속된 팀이 없음을 명시
