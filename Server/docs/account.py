from . import parameter

CHECK_GAME_KEY_GET = {
    'tags': ['Account'],
    'description': '게임키 유효성 확인',
    'parameters': [
        parameter('gameKey', '게임 인증키', 'uri', 'int')
    ],
    'responses': {
        '200': {
            'description': '유효한 인증키',
            'examples': {
                '': {
                    'gameKey': '게임키 들어갈거임'
                }
            }
        },
        '204': {
            'description': '잘못된 게임 인증키'
        }
    }
}

AUTH_POST = {
    'tags': ['Account'],
    'description': '로그인',
    'parameters': [
        parameter('gameKey', '게임 인증키', 'uri', 'int'),
        parameter('id', '아이디'),
        parameter('password', '비밀번호'),
        parameter('email', '이메일')
    ],
    'responses': {
        '200': {
            'description': '인증 또는 회원가입 성공',
            'examples': {
                '': {
                    'accessToken': '액세스 토오오오큰'
                }
            }
        },
        '204': {
            'description': '잘못된 게임 인증키'
        },
        '205': {
            'description': '잘못된 비밀번호'
        }
    }
}
