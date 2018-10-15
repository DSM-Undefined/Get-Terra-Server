from flasgger import swag_from
from flask_restful import reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from view.base_resource import BaseResource
from docs.team import TEAM_GET, TEAM_POST
from model import UserInfo, Club


class Team(BaseResource):

    @swag_from(TEAM_GET)
    def get(self):
        pass

    @swag_from(TEAM_POST)
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser
        parser.add_argument('team', type=str, required=True)
        payload = parser.parse_args()
        id_in_db = UserInfo.objects(userId=get_jwt_identity())

        if id_in_db:
            UserInfo.objects(userId=get_jwt_identity()).update_one(set__team=payload['team'])
            # user_info collection 의 사용자 정보 중 'team'을 업데이트

