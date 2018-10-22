from . import parameter

BOOTH_PUT = {
    'tags': ['Booth'],
    'description': '부스 등록',
    'parameters': [
        parameter('boothNameList', '부스 이름 리스트 ["ㅁㅁ", "ㅇㅇ"]', type='string list')
    ],
    'responses': {
        '201': {
            'description': '성공'
        },
        '205': {
            'description': '빈 리스트'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

BOOTH_DELETE = {
    'tags': ['Booth'],
    'description': '부스 삭제',
    'parameters': [
        parameter('boothName', '부스 이름')
    ],
    'responses': {
        '201': {
            'description': '성공'
        },
        '204': {
            'description': '해당 동아리 이름을 가진 동아리 없음'
        }
    }
}