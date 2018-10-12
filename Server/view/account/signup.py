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
        email_ = parser.parse_args()['email']
        id_ = parser.parse_args()['id']
        password_ = parser.parse_args()['password']
        # 이메일, ID, 비밀번호 파싱

        db_201 = {
            "userId": id_,
            "email": email_,
            "password": password_
        }

        if UserInfo.objects(userId__ne=id_) or UserInfo.object(email__ne=email_):
            UserInfo(userId=id_, email=email_, password=password_, team=1)
            # DB에 중복되는 닉네임이 없음을 확인하고 신규 회원 정보를 DB에 저장
            return 201
        else:
            return 205
