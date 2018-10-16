from flasgger import swag_from
from flask import request, jsonify, Response
from flask_jwt_extended import create_access_token
from datetime import timedelta

from view.base_resource import BaseResource
from model.UserInfo import UserInfo
from docs.account import AUTH_POST


class Auth(BaseResource):

    @swag_from(AUTH_POST)
    def post(self):
        payload = request.json

        user = UserInfo.objects(userId=payload['id'], password=self.encrypt_password(payload['password']))
        if user:
            return jsonify({"accessTocken": create_access_token(identity=payload['id'], expires_delta=timedelta(days=1))})

        return Response('', 401)

        # 로그인 성공시 액세스 토큰 및 리프레시 토큰을 반환
