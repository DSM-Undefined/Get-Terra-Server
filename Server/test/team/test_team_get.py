from test import TCBase, check_status_code


class TeamGetTest(TCBase):

    def team_get_request(self, game_key=100000):
        return self.client.get(
            '/team',
            headers={'Authorization': f'Bearer {self._create_access_token()}'}
        )

    @check_status_code(200)
    def test_success(self):
        return self.team_get_request()
