from flask import Response
import json

from test import TestBase


class SignupTest(TestBase):

    def __init__(self):
        super(SignupTest, self).__init__()

    def signup_request(self, email='python@istruly.sexy', id='NerdBear', password='nerd'):
        return self.client.post(
            '/signup',
            data=json.dumps(
                dict(emtil=email, id=id, password=password)
            )
        )

    def test_signup(self):
        # 계정 생성
        rv: Response = self.signup_request()
        self.assertEqual(rv.status_code, 201)

        # 이미 가입된 아이디, 이메일
        rv: Response = self.signup_request()
        self.assertEqual(rv.status_code, 201)

        # 이미 가입된 아이디
        rv: Response = self.signup_request(email='sm372181@gmail.com')
        self.assertEqual(rv.status_code, 205)

        # 이미 가입된 이메일
        rv: Response = self.signup_request(id='Sangmin')
        self.assertEqual(rv.status_code, 205)

        # 다른 아이디, 이메일로 가입
        rv: Response = self.signup_request(email='sm372181@gmail.com', id='Sangmin')
        self.assertEqual(rv.status_code, 201)
