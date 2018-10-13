from flasgger import swag_from
from flask_restful import Resource, reqparse
from flask import jsonify
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
        payload = parser.parse_args()

        id_in_db = UserInfo.objects(userId=payload['id'])
        correct_password = UserInfo.object(password=payload['password'])
        success_201 = {
            "accessToken": create_access_token(payload['id']),
            "refreshToken": create_refresh_token(payload['id'])
        }

        if id_in_db and correct_password:
            return jsonify(success_201), 201
        # 로그인 성공시 액세스 토큰 및 리프레시 토큰을 반환

        else:
            return 401
        # 로그인 실패시 status code 401 반환
