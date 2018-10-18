from docs import parameter

INIT_GAME_POST = {
    'tags': ['init'],
    'description': '게임 초기화',
    'parameters': [
        parameter('secretKey', 'SECRET_KEY'),
        parameter('start', '게임 시작 시간 {"year": 2018, "month": 10, "day": 20, "hour": 12}', type='dict'),
        parameter('end', '게임 끝시간 {"year": 2018, "month": 10, "day": 20, "hour": 12}', type='dict')
    ],
    'responses': {
        '201': {'description': '설정 성공'},
        '403': {'description': '권한없음 (잘못된 secretKey)'}
    }
}
