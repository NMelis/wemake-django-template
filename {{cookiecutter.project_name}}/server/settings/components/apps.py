# -*- coding: utf-8 -*-

from typing import Tuple

# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Security:
    'axes',

    # Your apps go here:
    'server.apps.common',
)
