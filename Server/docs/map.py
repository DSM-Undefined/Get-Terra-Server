from . import jwt_header

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
                    'map': {
                        'GRAM': 0,
                        '시나브로': 1,
                        'Undefined': 2,
                        'NoNamed': 3,
                        'LUNA': -1
                    },
                    'endTime': {'year': 2018, 'month': 10, 'day': 20, 'hour': 12, 'minute': 0}
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
                    'map': {
                        '1': {
                            'team': 3,
                            'booths': 20
                        },
                        '2': {
                            'team': 1,
                            'booths': 16
                        },

                        '3': {
                            'team': 2,
                            'booths': 9
                        },
                        '4': {
                            'team': 0,
                            'booths': 3
                        }
                    }
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
                    'map': {
                        'GRAM': True,
                        '시나브로': False,
                        'Undefined': True,
                        'NoNamed': None,
                        'LUNA': None
                    },
                    'myTeam': 1,
                    'endTime': {'year': 2018, 'month': 10, 'day': 20, 'hour': 12, 'minute': 0}
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