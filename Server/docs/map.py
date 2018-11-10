from . import jwt_header

MAP_GET = {
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
                    'myTeamColor': '58c9b9'
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