from json import loads

from test import TCBase, check_status_code
from test.requests import map_get_request


class MapGetTest(TCBase):

    @check_status_code(200)
    def test_success_map_get(self):
        rv = map_get_request(self)
        res_json = loads(rv.data, encoding='utf-8')

        self.assertEqual(res_json['myTeam'], self.test_user.team.team_id)
        self.assertEqual(res_json['myTeamColor'], self.test_user.team.team_color)

        map_ = res_json['map']
        for i in range(5):
            self.assertEqual(map_[f'booth{i}'], -1)
        return rv
