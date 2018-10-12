from . import jwt_header, parameter

SOLVE_GET = {
    'tags': ['Solve'],
    'description': '문제 get',
    'parameters': [
        jwt_header,
        parameter('clubId', '동아리 아이디', 'url')
    ],
    'responses': {
        '200': {
            'description': '성공',
            'examples': {
                '': {
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
        }
    }
}

SOLVE_POST = {
    'tags': ['Solve'],
    'description': '문제 정답 제출',
    'parameters': [
        jwt_header,
        parameter('clubCode', '동아리 아이디', 'url'),
        parameter('problemId', '문제 아이디', 'query'),
        parameter('answer', '''정답
        주관식: (str) 정답
        OX: (str) O / X
        4지 선다: (int) 정답 번호''', 'json')
    ],
    'responses': {
        '201': {
            'description': '정답'
        },
        '205': {
            'description': '오답'
        }
    }
}