import os
from datetime import datetime
from json import loads


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
            }
        ]
    }

    JSON_AS_ASCII = False

    JWT_SECRET_KEY = os.getenv('SECRET_KEY', 'nerd-bear')
    SECRET_KEY = os.getenv('SECRET_KEY', 'nerd-bear')
