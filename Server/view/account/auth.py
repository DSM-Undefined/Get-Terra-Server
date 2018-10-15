from flasgger import swag_from
from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token

from view.base_resource import BaseResource
from model.UserInfo import UserInfo
from docs.account import AUTH_POST


class Auth(Resource):

    @swag_from(AUTH_POST)
    def post(self):
        payload = request.json

        for user in UserInfo.objects:
            if user.userId == payload['id'] and user.password == payload['password']:
                return {
                    "accessTocken": create_access_token(identity=payload['id']),
                    "refreshToken": create_refresh_token(identity=payload['id'])
                       }, 201

        return {"result": "failure"}, 401

        # 로그인 성공시 액세스 토큰 및 리프레시 토큰을 반환
