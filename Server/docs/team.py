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
                        None,
                        [
                            '상미니'
                        ]
                    ]
            }
        }
    }
}

TEAM_POST = {
    'tags': ['Team'],
    'description': '팀 참가',
    'parameters': [
        jwt_header,
        parameter('team', '팀 종류\n0: blue\n1: green\n2: yellow\n3: violet', 'query string')
    ],
    'responses': {
        '201': {
            'description': '참가 성공'
        },
        '205': {
            'description': '팀원 초과'
        }
    }
}