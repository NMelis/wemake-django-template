# -*- coding: utf-8 -*-

from server.settings.components import config

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        # Choices are: postgresql_psycopg2, mysql, sqlite3, oracle
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        # Database name or filepath if using 'sqlite3':
        'NAME': config('POSTGRES_DB'),

        # You don't need these settings if using 'sqlite3':
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('DJANGO_DATABASE_HOST'),
        'PORT': config('DJANGO_DATABASE_PORT', cast=int),
        'CONN_MAX_AGE': config('CONN_MAX_AGE', cast=int, default=60),
    },
}
