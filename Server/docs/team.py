from . import parameter, jwt_header

TEAM_GET = {
    'tags': ['Team'],
    'description': '팀별 팀원 리스트\n 순서: blue, green, yellow, violet',
    'parameters': [
        jwt_header
    ],
    'responses': {
        '201': {
            'description': 'get 성공',
            'examples': {
                '': [
                        [
                            'ㅁㅁ',
                            'ㅇㅇ',
                            'ㄷㄷ'
                        ],
                        [
                            'aa',
                            'dd'
                        ],
                        [],
                        [
                            '상미니'
                        ]
                    ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

TEAM_POST = {
    'tags': ['Team'],
    'description': '팀 참가',
    'parameters': [
        jwt_header,
        parameter('team', '''팀 종류
        0: blue
        1: green
        2: yellow
        3: violet''', 'query string')
    ],
    'responses': {
        '201': {
            'description': '참가 성공'
        },
        '204': {
            'description': '이미 팀에 소속되어 있음'
        },
        '205': {
            'description': '팀원 초과, 잘못된 팀 번호'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}