from . import parameter

SIGNUP_POST = {
    'tags': ['Account'],
    'description': '회원가입',
    'parameters': [
        parameter('email', '이메일'),
        parameter('id', '아이디'),
        parameter('password', '비밀번호')
    ],
    'responses': {
        '201': {
            'description': '가입 완료'
        },
        '205': {
            'description': '중복 id 또는 email'
        }
    }
}

BOOTH_GET = {
    'tags': ['Booth'],
    'description': '부스 리스트',
    'parameters': [],
    'responses': {
        '200': {
            'description': 'get 성공'
        },
        '204': {
            'description': 'db에 부스가 없음'
        }
    }
}

BOOTH_POST = {
    'tags': ['Booth'],
    'description': '부스 등록',
    'parameters': [
        parameter('boothNameList', '부스 이름', type='string list')
    ],
    'responses': {
        '201': {
            'description': '성공'
        },
        '205': {
            'description': '빈 리스트'
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