from datetime import datetime, timedelta
from json import dumps

from model.booth import BoothModel
from test import TCBase, check_status_code


class SolvePostTest(TCBase):

    def solve_post_request(self, booth_name='booth0', problem_id=1, answer='1'):
        return self.client.post(
            f'/solve/{booth_name}',
            data=dumps(dict(problemId=problem_id, answer=answer)),
            content_type='application/json',
            headers={'Authorization': self.access_token}
        )

    @check_status_code(201)
    def test_success_solve_post(self):
        rv = self.solve_post_request()
        booth = BoothModel.objects(booth_name='booth0').first()

        self.assertEqual(booth.own_team, self.test_user.team)
        return rv

    @check_status_code(204)
    def test_wrong_problem_id(self):
        return self.solve_post_request(problem_id=2)

    @check_status_code(204)
    def test_wrong_booth_id(self):
        return self.solve_post_request(booth_name='wrong')

    @check_status_code(205)
    def test_wrong_answer(self):
        return self.solve_post_request(answer='2')

    @check_status_code(406)
    def test_before_start_game(self):
        self.test_game.start_time = datetime.now() + timedelta(days=1)
        self.test_game.save()
        return self.solve_post_request()

    @check_status_code(408)
    def test_delay(self):
        self.solve_post_request()
        return self.solve_post_request()

    @check_status_code(412)
    def test_after_end_game(self):
        self.test_game.end_time = datetime.now() - timedelta(days=1)
        self.test_game.save()
        return self.solve_post_request()
