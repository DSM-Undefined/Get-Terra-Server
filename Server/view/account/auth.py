from flasgger import swag_from
from flask import request, jsonify, Response
from flask_jwt_extended import create_access_token
from datetime import timedelta

from view.base_resource import BaseResource
from model.User import UserModel
from docs.account import AUTH_POST


class Auth(BaseResource):

    @swag_from(AUTH_POST)
    def post(self):
        payload = request.json

        pw = self.encrypt_password(payload['password'])
        user: UserModel = UserModel.objects(userId=payload['id'], password=pw).first()
        if user:
            return jsonify({"accessTocken": create_access_token(identity=user.userId, expires_delta=timedelta(days=1))})

        return Response('', 401)
