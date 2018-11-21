from test import TCBase, check_status_code
from test.requests import team_post_request
from model.user import UserModel


class TeamPostTest(TCBase):

    def check_user_team(self, user_id='test', team_number=0):
        user = UserModel.objects(user_id=user_id).first()
        self.assertEqual(user.team.team_id, team_number)

    @check_status_code(201)
    def test_success_team_post(self):
        rv = team_post_request(self)
        self.check_user_team(team_number=1)
        return rv

    @check_status_code(204)
    def test_already_has_team(self):
        team_post_request(self)
        self.check_user_team(team_number=1)

        rv = team_post_request(self, team_number=2)
        self.check_user_team(team_number=1)
        return rv

    @check_status_code(205)
    def test_wrong_team_number1(self):
        rv = team_post_request(self, team_number=-1)
        self.check_user_team()
        return rv

    @check_status_code(205)
    def test_wrong_team_number2(self):
        rv = team_post_request(self, team_number=5)
        self.check_user_team()
        return rv
