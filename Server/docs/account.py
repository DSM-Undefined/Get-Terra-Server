from . import parameter
SIGNUP_POST = {
    'tags': ['Account'],
    'description': '회원가입',
    'parameters': [
        parameter('email', '이메일'),
        parameter('id', '아이디'),
        parameter('password', '비밀번호')
    ],
    'responses': {
        '201': {
            'description': '가입 완료'
        },
        '205': {
            'description': '중복 id 또는 email'
        }
    }
}

AUTH_POST = {
    'tags': ['Account'],
    'description': '로그인',
    'parameters': [
        parameter('id', '아이디'),
        parameter('password', '비밀번호')
    ],
    'responses': {
        '200': {
            'description': '로그인 성공',
            'examples': {
                '': {
                    'accessToken': '액세스 토오오오큰'
                }
            }
        },
        '401': {
            'description': '로그인 실패'
        }
    }
}