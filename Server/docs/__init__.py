jwt_header = {
    'name': 'Authorization',
    'description': 'JWT token',
    'in': 'header',
    'type': 'str',
    'required': True
}


def parameter(name, description, in_='json', type='str', required=True):
    return {
        'name': name,
        'description': description,
        'in': in_,
        'type': type,
        'required': required
    }