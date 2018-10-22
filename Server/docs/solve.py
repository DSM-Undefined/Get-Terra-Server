from . import jwt_header, parameter

SOLVE_GET = {
    'tags': ['Solve'],
    'description': '문제 get',
    'parameters': [
        jwt_header,
        parameter('boothName', '부스 이름', 'url')
    ],
    'responses': {
        '200': {
            'description': '성공',
            'examples': {
                '': {
                    'boothName': '부스 이름',
                    'problemId': '문제 아이디',
                    'content': '문제 내용',
                    'choices': [
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
            'description': '이미 해당팀에서 점령한 부스임'
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
        parameter('boothName', '부스 이름', 'url'),
        parameter('problemId', '문제 아이디'),
        parameter('answer', '정답 (보기 내용)')
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

SOLVE_PUT = {
    'tags': ['Solve'],
    'description': '문제 등록',
    'parameters': [
        parameter('sercretKey', '시크릿 키'),
        parameter('problems', '문제 리스트 ([{"problemId": 문제 번호(int), "content": "문제 내용(str)", "answer": "정답(str)", "choices": 4지선다 보기 (["1번", "2번", "3번", "4번"])}]))', type='dict (map)')
    ],
    'response': {
        '201': {'description': '정답'},
        '403': {'description': '잘못된 secret key'}
    }
}