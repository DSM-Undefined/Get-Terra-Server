from datetime import datetime, timedelta
from json import dumps

from model.booth import BoothModel
from test import TCBase, check_status_code
from test.requests import solve_post_request


class SolvePostTest(TCBase):

    @check_status_code(201)
    def test_success_solve_post(self):
        rv = solve_post_request(self)
        booth = BoothModel.objects(booth_name='booth0').first()

        self.assertEqual(booth.own_team, self.test_user.team)
        return rv

    @check_status_code(204)
    def test_wrong_problem_id(self):
        return solve_post_request(self, problem_id=2)

    @check_status_code(204)
    def test_wrong_booth_id(self):
        return solve_post_request(self, booth_name='wrong')

    @check_status_code(205)
    def test_wrong_answer(self):
        return solve_post_request(self, answer='2')

    @check_status_code(406)
    def test_before_start_game(self):
        self.test_game.start_time = datetime.now() + timedelta(days=1)
        self.test_game.save()
        return solve_post_request(self)

    @check_status_code(408)
    def test_delay(self):
        solve_post_request(self)
        return solve_post_request(self)

    @check_status_code(412)
    def test_after_end_game(self):
        self.test_game.end_time = datetime.now() - timedelta(days=1)
        self.test_game.save()
        return solve_post_request(self)
