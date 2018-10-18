import os
from datetime import datetime


class Config:
    SERVICE_NAME = 'Get Terra'

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'host': 'ec2.istruly.sexy:1234',
        'basePath': '/',
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Account',
                'description': '계정 관련 API'
            },
            {
                'name': 'Map',
                'description': '맵 관련 API'
            },
            {
                'name': 'Solve',
                'description': '문제 풀이 관련 API'
            },
            {
                'name': 'Team',
                'description': '팀 관련 API'
            },
            {
                'name': 'Booth',
                'description': '부스 관련 api (서버 외엔 터치 x)'
            },
            {
                'name': 'Init',
                'description': '게입 초기화 api (서버 외엔 터치 X)'
            }
        ]
    }

    JSON_AS_ASCII = False
    # UTF-8로 인코딩된 JSON을 반환하기 위해(아마도) 설정

    JWT_SECRET_KEY = os.getenv('SECRET_KEY', 'nerd-bear')
    SECRET_KEY = os.getenv('SECRET_KEY', 'nerd-bear')
    START_TIME = datetime(2018, 10, 20, 12)
    END_TIME = datetime(2018, 10, 20, 13)
