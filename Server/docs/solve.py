from . import jwt_header, parameter

SOLVE_GET = {
    'tags': ['Solve'],
    'description': '문제 get',
    'parameters': [
        jwt_header,
        parameter('boothName', '동아리 이름', 'url')
    ],
    'responses': {
        '200': {
            'description': '성공',
            'examples': {
                '': {
                    'boothName': '동아리 이름',
                    'problemId': '문제 아이디',
                    'question': '문제 내용',
                    'problemType': '''(int) 0 주관식
                    1 4지선다
                    2 OX''',
                    'choices (4지선다만)': [
                        '1번 보기',
                        '2번 보기',
                        '3번 보기',
                        '4번 보기'
                    ]
                }
            }
        },
        '204': {
            'description': '해당 부스아이디에 해당하는 부스 없음'
        },
        '205': {
            'description': '이미 팀에서 점령한 부스임'
        },
        '401': {
            'description': 'request header 에 access token 없음 '
        },
        '403': {
            'description': '권한 없음'
        },
        '406': {
            'description': '게임 시작 전'
        },
        '408': {
            'description': '딜레이 시간'
        },
        '412': {
            'description': '게임 종료'
        }
    }
}

SOLVE_POST = {
    'tags': ['Solve'],
    'description': '문제 정답 제출',
    'parameters': [
        jwt_header,
        parameter('boothCode', '동아리 아이디', 'url'),
        parameter('problemId', '문제 아이디'),
        parameter('answer', '''정답
        주관식: (str) 정답
        OX: (str) O / X
        4지 선다: (int) 정답 번호''')
    ],
    'responses': {
        '201': {
            'description': '정답'
        },
        '204': {
            'description:': '잘못된 문제 아이디 또는 잘못된 동아리 아이디'
        },
        '205': {
            'description': '오답'
        },
        '401': {
            'description': 'request header 에 access token 없음 '
        },
        '403': {
            'description': '권한 없음'
        },
        '406': {
            'description': '게임 시작 전'
        },
        '408': {
            'description': '딜레이 시간'
        },
        '412': {
            'description': '게임 종료'
        }
    }
}