from test import TCBase, check_status_code
from test.requests import auth_request


class AuthTest(TCBase):

    @check_status_code(200)
    def test_success_create_user(self):
        return auth_request(self)

    @check_status_code(200)
    def test_success_auth_again(self):
        auth_request(self)
        return auth_request(self)

    @check_status_code(204)
    def test_wrong_game_key(self):
        return auth_request(self, game_key=111111)

    @check_status_code(205)
    def test_fail_to_auth(self):
        auth_request(self)
        return auth_request(self, password='Sangmin')
