from test import TCBase, check_status_code


class CheckGameKeyTest(TCBase):

    def check_game_key_request(self, game_key=100000):
        return self.client.get(
            '/auth/'+str(game_key)
        )

    @check_status_code(204)
    def test_wrong_game_key(self):
        return self.check_game_key_request(111111)

    @check_status_code(200)
    def test_success_check_game_key(self):
        return self.check_game_key_request()
