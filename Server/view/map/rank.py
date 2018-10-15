from flasgger import swag_from
from flask import jsonify

from view.base_resource import BaseResource
from docs.map import RANK_MAP_GET
from model import Club


class Rank(BaseResource):

    @swag_from(RANK_MAP_GET)
    def get(self):
        sort_args = [
            [club.clubId, ] for club in Club.objects()
        ]
        # 아직 정렬 기능 미구현
        # (점령한 땅의 수) 가 뭔지 모르겠음

        return jsonify(sort_args), 200
