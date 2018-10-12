from flasgger import swag_from
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token

from view.base_resource import BaseResource
from docs.account import AUTH_POST
from model import UserInfo


class Auth(BaseResource):

    @swag_from(AUTH_POST)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        id_ = parser.parse_args()['id']
        password_ = parser.parse_args()['password']

        id_in_db = UserInfo.objects(userId=id_)
        correct_password = UserInfo.object(password=password_)
        success_201 = {
            "accessToken": create_access_token(id_),
            "refreshToken": create_refresh_token(id_)
        }

        if id_in_db and correct_password:
            return success_201, 201
        # 로그인 성공시 액세스 토큰 및 리프레시 토큰을 반환

        else:
            return 401
        # 로그인 실패시 status code 401 반환
