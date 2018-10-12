from . import parameter

TEAM_GET = {
    'tags': ['Team'],
    'description': '팀별 팀원 리스트',
    'parameters': [
        parameter('team', '팀 종류', 'query string')
    ],
    'responses': {
        '201': {
            'description': 'get 성공',
            'examples': {
                '': {
                    {
                        'blue': [
                            'ㅁㅁ',
                            'ㅇㅇ',
                            'ㄷㄷ'
                        ],
                        'green': [
                            'aa',
                            'dd'
                        ],
                        'yellow': None,
                        'violet': [
                            '상미니'
                        ]
                    }
                }
            }
        }
    }
}