from datetime import datetime, timedelta
from json import loads

from test import TCBase, check_status_code


class SolveGetTest(TCBase):

    def solve_get_request(self, booth_name='booth0'):
        return self.client.get(
            f'/solve/{booth_name}',
            headers={'Authorization': self.access_token}
        )

    def team_post_request(self, team_number=1):
        return self.client.post(
            f'/team?team={team_number}',
            headers={'Authorization': self.access_token}
        )

    @check_status_code(200)
    def test_success(self):
        self.team_post_request()
        rv = self.solve_get_request()
        res_json = loads(rv.data, encoding='utf-8')

        self.assertEqual(res_json['boothName'], 'booth0')
        self.assertEqual(res_json['problemId'], 1)
        self.assertEqual(res_json['content'], 'test')
        self.assertEqual(res_json['choices'], ['1', '2', '3', '4'])
        return rv

    @check_status_code(204)
    def test_wrong_booth_name(self):
        return self.solve_get_request(booth_name='wrong')

    @check_status_code(406)
    def test_before_start_game(self):
        self.test_game.start_time = datetime.now() + timedelta(days=1)
        self.test_game.save()
        return self.solve_get_request()

    @check_status_code(412)
    def test_after_end_game(self):
        self.test_game.end_time = datetime.now() - timedelta(days=1)
        self.test_game.save()
        return self.solve_get_request()
