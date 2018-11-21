from datetime import datetime, timedelta
from json import loads

from test import TCBase, check_status_code
from test.requests import team_post_request, solve_get_request


class SolveGetTest(TCBase):

    @check_status_code(200)
    def test_success(self):
        team_post_request(self)
        rv = solve_get_request(self)
        res_json = loads(rv.data, encoding='utf-8')

        self.assertEqual(res_json['boothName'], 'booth0')
        self.assertEqual(res_json['problemId'], 1)
        self.assertEqual(res_json['content'], 'test')
        self.assertEqual(res_json['choices'], ['1', '2', '3', '4'])
        return rv

    @check_status_code(204)
    def test_wrong_booth_name(self):
        return solve_get_request(self, booth_name='wrong')

    @check_status_code(406)
    def test_before_start_game(self):
        self.test_game.start_time = datetime.now() + timedelta(days=1)
        self.test_game.save()
        return solve_get_request(self)

    @check_status_code(412)
    def test_after_end_game(self):
        self.test_game.end_time = datetime.now() - timedelta(days=1)
        self.test_game.save()
        return solve_get_request(self)
