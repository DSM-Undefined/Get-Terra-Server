from flasgger import swag_from
from flask_restful import reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from view.base_resource import BaseResource
from docs.solve import SOLVE_GET, SOLVE_POST


class Solve(BaseResource):

    @swag_from(SOLVE_GET)
    @jwt_required
    def get(self, clubId):
        user_id = get_jwt_identity()
        parser = reqparse.RequestParser
        parser.add_argument('clubId', type=str, required=true)
        payload = parser.parse_args()

    @swag_from(SOLVE_POST)
    def post(self, clubId):
        pass
