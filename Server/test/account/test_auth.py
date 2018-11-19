from json import dumps, loads

from test import TCBase, check_status_code


class AuthTest(TCBase):

    def auth_request(self, game_key=100000, id_='Nerd-Bear', password='NerdBear', email='python@istruly.sexy'):
        return self.client.post(
            '/auth/'+str(game_key),
            data=dumps(dict(id=id_, password=password, email=email)),
            content_type='application/json'
        )

    @check_status_code(200)
    def test_success_create_user(self):
        return self.auth_request()

    @check_status_code(200)
    def test_success_auth_again(self):
        self.auth_request()
        return self.auth_request()

    @check_status_code(204)
    def test_wrong_game_key(self):
        return self.auth_request(game_key=111111)

    @check_status_code(205)
    def test_fail_to_auth(self):
        self.auth_request()
        return self.auth_request(password='Sangmin')
