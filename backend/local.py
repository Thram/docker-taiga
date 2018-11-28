# -*- coding: utf-8 -*-
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example
from .common import *
import environ


env = environ.Env()
DEBUG = env('DJANGO_DEBUG', cast=bool, default=False)
PUBLIC_REGISTER_ENABLED = env(
    'PUBLIC_REGISTER_ENABLED', cast=bool, default=True
)

SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS', cast=list, default=['*'])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB', default='taiga'),
        'USER': env('POSTGRES_USER', default='taiga'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='taiga'),
        'HOST': env('POSTGRES_HOST', default='postgresql'),
        'PORT': '',
    }
}

TAIGA_HOSTNAME = env('HOSTNAME', default='localhost')

_HTTP = 'https' if env('SSL_ENABLED', cast=bool, default=False) else 'http'

SITES = {
    "api": {
        "scheme": _HTTP,
        "domain": TAIGA_HOSTNAME,
        "name": "api"
    },
    "front": {
        "scheme": _HTTP,
        "domain": TAIGA_HOSTNAME,
        "name": "front"
    },
}

SITE_ID = "api"

MEDIA_URL = "{}://{}/media/".format(_HTTP, TAIGA_HOSTNAME)
STATIC_URL = "{}://{}/static/".format(_HTTP, TAIGA_HOSTNAME)
MEDIA_ROOT = '/taiga_backend/media'
STATIC_ROOT = '/taiga_backend/static-root'

# Async
# see celery_local.py
# BROKER_URL = 'amqp://taiga:taiga@rabbitmq:5672/taiga'
EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://taiga:taiga@rabbitmq:5672/taiga"}

# see celery_local.py
CELERY_ENABLED = True

# Mail settings
# if env('USE_ANYMAIL', cast=bool, default=False):
#     INSTALLED_APPS += ['anymail']
#     ANYMAIL = {
#         "MAILGUN_API_KEY": env('ANYMAIL_MAILGUN_API_KEY'),
#     }
#     EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"
#     DEFAULT_FROM_EMAIL = "Taiga <{}>".format(env('DJANGO_DEFAULT_FROM_EMAIL'))

# Cache
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
#         "LOCATION": "unique-snowflake"
#     }
# }

# Importers
IMPORTERS = {
    "trello": {
        "active": env('IMPORTER_TRELLO_ENABLED', cast=bool, default=False),
        "api_key": env('TRELLO_API_KEY', default=''),
        "secret_key": env('TRELLO_OAUTH_SECRET', default='')
    }
}

print("Setup finished")
