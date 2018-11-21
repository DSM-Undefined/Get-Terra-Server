from json import loads

from test import TCBase, check_status_code


class MapGetTest(TCBase):

    def map_get_request(self):
        return self.client.get(
            '/map',
            headers={'Authorization': self.access_token}
        )

    @check_status_code(200)
    def test_success_map_get(self):
        rv = self.map_get_request()
        res_json = loads(rv.data, encoding='utf-8')

        self.assertEqual(res_json['myTeam'], self.test_user.team.team_id)
        self.assertEqual(res_json['myTeamColor'], self.test_user.team.team_color)

        map_ = res_json['map']
        for i in range(5):
            self.assertEqual(map_[f'booth{i}'], -1)
        return rv
