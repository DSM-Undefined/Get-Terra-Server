from json import dumps


def check_game_key_request(self, game_key=100000):
    return self.client.get(
        '/auth/' + str(game_key)
    )


def auth_request(self, game_key=100000, id_='Nerd-Bear', password='NerdBear', email='python@istruly.sexy'):
    return self.client.post(
        '/auth/'+str(game_key),
        data=dumps(dict(id=id_, password=password, email=email)),
        content_type='application/json'
    )


def map_get_request(self):
    return self.client.get(
        '/map',
        headers={'Authorization': self.access_token}
    )


def solve_get_request(self, booth_name='booth0'):
    return self.client.get(
        f'/solve/{booth_name}',
        headers={'Authorization': self.access_token}
    )


def solve_post_request(self, booth_name='booth0', problem_id=1, answer='1'):
    return self.client.post(
        f'/solve/{booth_name}',
        data=dumps(dict(problemId=problem_id, answer=answer)),
        content_type='application/json',
        headers={'Authorization': self.access_token}
    )


def team_get_request(self):
    return self.client.get(
        '/team',
        headers={'Authorization': self.access_token}
    )


def team_post_request(self, team_number=1):
    return self.client.post(
        f'/team?team={team_number}',
        headers={'Authorization': self.access_token}
    )
