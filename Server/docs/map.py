from . import jwt_header, parameter

WEB_MAP_GET = {
    'tags': ['Map'],
    'description': '웹 현재 맵 상황',
    'parameters': [],
    'responses': {
        '200': {
            'description': """get 성공
            -1: 아직 점령되지 않음
            0: blue
            1: green
            2: yellow
            3: violet""",
            'examples': {
                '': {
                    'map': [
                        ['그램', 0],
                        ['시나브로', 1],
                        ['언디파인드', 2],
                        ['GG', 3],
                        ['스위트팹', -1]
                    ]
                }
            }
        },
        '406': {
            'description': '게임 시작 전'
        },
        '412': {
            'description': '게임 종료'
        }
    }
}

RANK_MAP_GET = {
    'tags': ['Map'],
    'description': '현재 랭킹',
    'parameters': [],
    'responses': {
        '200': {
            'description': 'get 성공 (랭킹 순 정렬)',
            'examples': {
                '': {
                    'map': [
                        ['(팀 번호)', '(점령한 땅의 수)'],
                        [3, 20],
                        [1, 16],
                        [2, 9],
                        [0, 3],
                        [-1, 0]
                    ]
                }
            }
        },
        '406': {
            'description': '게임 시작 전'
        },
        '412': {
            'description': '게임 종료'
        }
    }
}

ANDROID_MAP_GET = {
    'tags': ['Map'],
    'description': '안드로이드 현재 맵 상황',
    'parameters': [jwt_header],
    'responses': {
        '200': {
            'description': """get 성공
            True: 우리팀이 점령함
            False: 다른팀이 점령함
            Null: 아직 점령이 안됨
            """,
            'examples': {
                '': {
                    'map': [
                        ['그램', True],
                        ['시나브로', False],
                        ['언디파인드', True],
                        ['GG', None],
                        ['스위트팹', None]
                    ]
                }
            }
        },
        '401': {
            'description': 'request header 에 access token 없음 '
        },
        '403': {
            'description': '권한 없음'
        }
    }
}