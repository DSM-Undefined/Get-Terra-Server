from test import TCBase, check_status_code
from test.requests import check_game_key_request


class CheckGameKeyTest(TCBase):

    @check_status_code(200)
    def test_success_check_game_key(self):
        return check_game_key_request(self)

    @check_status_code(204)
    def test_wrong_game_key(self):
        return check_game_key_request(self, 111111)
