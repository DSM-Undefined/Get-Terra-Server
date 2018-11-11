def parameter(name, description, in_='json', type='str', required=True):
    return {
        'name': name,
        'description': description,
        'in': in_,
        'type': type,
        'required': required
    }


jwt_header = ('Authorization', 'JWT Token', 'header')
gameKey = parameter('gameKey', '게임 인증키', 'uri', 'int')
