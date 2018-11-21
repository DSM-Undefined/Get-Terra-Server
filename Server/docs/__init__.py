def parameter(name, description, in_='json', type='str', required=True):
    return {
        'name': name,
        'description': description,
        'in': in_,
        'type': type,
        'required': required
    }


jwt_header = parameter('Authorization', 'JWT Token', 'header')
game_key = parameter('gameKey', '게임 인증키', 'uri', 'int')
