from . import parameter, jwt_header

TEAM_GET = {
    'tags': ['Team'],
    'description': '팀별 팀원 리스트',
    'parameters': [
        jwt_header
    ],
    'responses': {
        '200': {
            'description': 'get 성공',
            'examples': {
                '': {
                    'teamCount': 4,
                    '1': {
                        'teamColor': '#aaaaaa',
                        'member': [
                            'ㅁㅁ',
                            'ㅇㅇ',
                            'ㄷㄷ'
                        ],
                    },
                    '2': {
                        'teamColor': '#bbbbbb',
                        'member': [
                            'aa',
                            'dd'
                        ]
                    },
                    '3': {
                        'teamColor': '#5a4b4d',
                        'member': []
                    },
                    '4': {
                        'teamColor': '#73847d',
                        'member': ['상민이']
                    }
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

TEAM_POST = {
    'tags': ['Team'],
    'description': '팀 참가',
    'parameters': [
        jwt_header,
        parameter('team', '팀 넘버', 'query string', 'int')
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
        '401': {
            'description': 'request header 에 access token 없음 '
        },
        '403': {
            'description': '권한 없음'
        }
    }
}