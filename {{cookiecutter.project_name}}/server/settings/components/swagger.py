# -*- coding: utf-8 -*-

SWAGGER_SETTINGS = {
    'SUPPORTED_SUBMIT_METHOD': ['get', 'post', 'put', 'delete'],
    'USE_SESSION_AUTH': True,
    'LOGIN_URL': '/admin',
    'JSON_EDITOR': True,
    'LOGOUT_URL': '/admin/logout',
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
    'APIS_SORTER': 'alpha',
    'SHOW_REQUEST_HEADERS': True,
    'VALIDATOR_URL': None,
    'DEFAULT_MODEL_RENDERING': 'example',
}

LOGOUT_URL = '/admin/logout'
