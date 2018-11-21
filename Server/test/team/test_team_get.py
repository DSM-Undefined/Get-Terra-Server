from test import TCBase, check_status_code
from test.requests import team_get_request


class TeamGetTest(TCBase):

    @check_status_code(200)
    def test_success(self):
        return team_get_request(self)
