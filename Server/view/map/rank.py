from flasgger import swag_from
from flask import jsonify

from view.base_resource import BaseResource
from docs.map import RANK_MAP_GET
from model.Booth import BoothModel


class Rank(BaseResource):

    @swag_from(RANK_MAP_GET)
    def get(self):
        map_ = [[-1, 0], [0, 0], [1, 0], [2, 0], [3, 0]]

        for booth in BoothModel.objects():
            map_[booth.ownTeam + 1][1] += 1
        map_.sort(key=lambda a: a[1], reverse=True)

        return jsonify(map_), 200
