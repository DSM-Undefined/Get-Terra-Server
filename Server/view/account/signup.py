import json
from flasgger import swag_from
from flask_restful import reqparse, Resource
from flask import request, Response, jsonify
from mongoengine import *


from view.base_resource import BaseResource
from docs.account import SIGNUP_POST
from model.UserInfo import UserInfo


class Signup(Resource):
    @swag_from(SIGNUP_POST)
    def post(self):

        payload = request.json
        # 이메일, ID, 비밀번호 파싱

        for user in UserInfo.objects:
            if user.userId == payload['id']:
                if user.password != payload['password'] or user.password != payload['email']:
                    UserInfo.objects(userId=payload['id']).update_one(set__password=payload['password'],
                                                                      set__email=payload['email'])
                    return {"result": "changed successful"}, 201
                return {"result": "failure"}, 205

        UserInfo(userId=payload['id'], email=payload['email'], password=payload['password'], team=-1).save()
        return {"return": "success"}, 201

        # DB에 중복되는 닉네임이 없음을 확인하고 신규 회원 정보를 DB에 저장
        # 초기 유저 정보에는 'team'을 -1로 두어 현재 소속된 팀이 없음을 명시
        # userId가 같더라도 password 나 email 이 다를 경우 유저 정보를 업데이트
