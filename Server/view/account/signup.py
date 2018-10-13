from flasgger import swag_from
from flask_restful import reqparse

from view.base_resource import BaseResource
from docs.account import SIGNUP_POST
from model import UserInfo


class Signup(BaseResource):

    @swag_from(SIGNUP_POST)
    def post(self):
        parser = reqparse.RequestParser
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('id', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        payload = parser.parse_args()
        # 이메일, ID, 비밀번호 파싱

        if UserInfo.objects(userId__ne=payload['id']) or UserInfo.object(email__ne=payload['email']):
            UserInfo(userId=payload['id'], email=payload['email'], password=payload['password'], team=-1)
            # DB에 중복되는 닉네임이 없음을 확인하고 신규 회원 정보를 DB에 저장
            # 초기 유저 정보에는 team을 -1로 두어 현재 소속된 팀이 없음을 명시하였습니다.
            return 201
        else:
            return 205
