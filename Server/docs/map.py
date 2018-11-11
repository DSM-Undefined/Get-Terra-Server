from . import jwt_header

MAP_GET = {
    'tags': ['Map'],
    'description': '안드로이드 현재 맵 상황',
    'parameters': [jwt_header],
    'responses': {
        '200': {
            'description': """get 성공
            1: 우리팀이 점령함
            0: 다른팀이 점령함
            -1: 아직 점령이 안됨
            """,
            'examples': {
                '': {
                    'map': {
                        'GRAM': 1,
                        '시나브로': 0,
                        'Undefined': 1,
                        'NoNamed': -1,
                        'LUNA': -1
                    },
                    'myTeam': 3,
                    'myTeamColor': '#58c9b9'
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