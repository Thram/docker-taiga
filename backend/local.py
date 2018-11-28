# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .common import *
import environ


env = environ.Env()

#########################################
# GENERIC
#########################################

DEBUG = env('DEBUG', cast=bool, default=False)

#########################################
# SET CONFIG
#########################################

CONFIG = {
    'POSTGRES_DB': env('POSTGRES_DB', default='taiga'),
    'POSTGRES_USER': env('POSTGRES_USER', default='taiga'),
    'POSTGRES_PASSWORD': env('POSTGRES_PASSWORD', default='taiga'),
    'POSTGRES_HOST': env('POSTGRES_HOST', default='postgresql'),
    'POSTGRES_PORT': env('POSTGRES_PORT', default=5432),
    'HOSTNAME': env('HOSTNAME', default='localhost'),
    'SSL_ENABLED': env('SSL_ENABLED', cast=bool, default=False),
    'DEFAULT_FROM_EMAIL': env('EMAIL_FROM_DEFAULT', default='john@doe.com'),
    'EMAIL_USE_TLS': env('EMAIL_USE_TLS', cast=bool, default=True),
    # You cannot use both (TLS and SSL) at the same time!,
    'EMAIL_USE_SSL': env('EMAIL_USE_SSL', cast=bool, default=False),
    'EMAIL_HOST': env('EMAIL_USE_SSL', default='smtp.gmail.com'),
    'EMAIL_PORT': env('EMAIL_PORT', default=587),
    'EMAIL_HOST_USER': env('EMAIL_HOST_USER', default='youremail@gmail.com'),
    'EMAIL_HOST_PASSWORD': env('EMAIL_HOST_PASSWORD', default='yourpassword'),
    'PUBLIC_REGISTER_ENABLED': env('PUBLIC_REGISTER_ENABLED', cast=bool, default=True),
    'USER_EMAIL_ALLOWED_DOMAINS': env('USER_EMAIL_ALLOWED_DOMAINS', default=None),
    'RABBITMQ_USER': env('RABBITMQ_USER',  default='taiga'),
    'RABBITMQ_PASSWORD': env('RABBITMQ_PASSWORD',  default='taiga'),
    'RABBITMQ_VHOST': env('RABBITMQ_VHOST',  default='taiga'),
    'RABBITMQ_HOST': env('RABBITMQ_HOST',  default='rabbitmq'),
    'RABBITMQ_PORT': env('RABBITMQ_PORT',  default=5672),
    'IMPORTER_GITHUB_ENABLED': env('IMPORTER_GITHUB_ENABLED', cast=bool, default=False),
    'GITHUB_URL': env('GITHUB_URL', default=None),
    'GITHUB_API_URL': env('GITHUB_API_URL', default=None),
    'GITHUB_API_CLIENT_ID': env('GITHUB_API_CLIENT_ID', default=None),
    'GITHUB_API_CLIENT_SECRET': env('GITHUB_API_CLIENT_SECRET', default=None),
    'IMPORTER_TRELLO_ENABLED': env('IMPORTER_TRELLO_ENABLED', cast=bool, default=False),
    'TRELLO_API_KEY': env('TRELLO_API_KEY', default=None),
    'TRELLO_OAUTH_SECRET': env('TRELLO_OAUTH_SECRET', default=None),
    'IMPORTER_JIRA_ENABLED': env('IMPORTER_JIRA_ENABLED', cast=bool, default=False),
    'JIRA_CONSUMER_KEY': env('JIRA_CONSUMER_KEY', default=None),
    'JIRA_CERT': env('JIRA_CERT', default=None),
    'JIRA_PUB_CERT': env('JIRA_PUB_CERT', default=None),
    'IMPORTER_ASANA_ENABLED': env('IMPORTER_ASANA_ENABLED', cast=bool, default=False),
    'ASANA_APP_ID': env('ASANA_APP_ID', default=None),
    'ASANA_APP_SECRET': env('ASANA_APP_SECRET', default=None),
}

# ADMINS = (
#    ("Admin", "example@example.com"),
# )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONFIG['POSTGRES_DB'],
        'USER': CONFIG['POSTGRES_USER'],
        'PASSWORD': CONFIG['POSTGRES_PASSWORD'],
        'HOST': CONFIG['POSTGRES_HOST'],
        'PORT': CONFIG['POSTGRES_PORT'],
    }
}

TAIGA_HOSTNAME = CONFIG['HOSTNAME']

_HTTP = 'https' if CONFIG['SSL_ENABLED'] else 'http'

FRONT_SCHEME = _HTTP
FRONT_DOMAIN = TAIGA_HOSTNAME

SITES = {
    "api": {
        "scheme": FRONT_SCHEME,
        "domain": FRONT_DOMAIN,
        "name": "api"
    },
    "front": {
        "scheme": FRONT_SCHEME,
        "domain": FRONT_DOMAIN,
        "name": "front"
    },
}


SITE_ID = "api"

TAIGA_URL = f"{_HTTP}://{TAIGA_HOSTNAME}"
MEDIA_URL = f"{TAIGA_URL}/media/"
STATIC_URL = f"{TAIGA_URL}/static/"
MEDIA_ROOT = '/taiga_backend/media'
STATIC_ROOT = '/taiga_backend/static-root'


#########################################
# THROTTLING
#########################################

# REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon-write": "20/min",
#    "user-write": None,
#    "anon-read": None,
#    "user-read": None,
#    "import-mode": None,
#    "import-dump-mode": "1/minute",
#    "create-memberships": None,
#    "login-fail": None,
#    "register-success": None,
#    "user-detail": None,
#    "user-update": None,
# }

# This list should containt:
#  - Tiga users IDs
#  - Valid clients IP addresses (X-Forwarded-For header)
# REST_FRAMEWORK["DEFAULT_THROTTLE_WHITELIST"] = []


#########################################
# MAIL SYSTEM SETTINGS (Default setup GMAIL)
#########################################

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = CONFIG['DEFAULT_FROM_EMAIL']
EMAIL_USE_TLS = CONFIG['EMAIL_USE_TLS']
# You cannot use both (TLS and SSL) at the same time!
EMAIL_USE_SSL = CONFIG['EMAIL_USE_SSL']
EMAIL_HOST = CONFIG['EMAIL_USE_SSL']
EMAIL_PORT = CONFIG['EMAIL_PORT']
EMAIL_HOST_USER = CONFIG['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = CONFIG['EMAIL_HOST_PASSWORD']

#########################################
# REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = CONFIG['PUBLIC_REGISTER_ENABLED']

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
USER_EMAIL_ALLOWED_DOMAINS = CONFIG['USER_EMAIL_ALLOWED_DOMAINS']

# PUCLIC OR PRIVATE NUMBER OF PROJECT PER USER
# MAX_PRIVATE_PROJECTS_PER_USER = None # None == no limit
# MAX_PUBLIC_PROJECTS_PER_USER = None # None == no limit
# MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None # None == no limit
# MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None # None == no limit

# GITHUB SETTINGS
GITHUB_URL = CONFIG['GITHUB_URL']
GITHUB_API_URL = CONFIG['GITHUB_API_URL']
GITHUB_API_CLIENT_ID = CONFIG['GITHUB_API_CLIENT_ID']
GITHUB_API_CLIENT_SECRET = CONFIG['GITHUB_API_CLIENT_SECRET']


#########################################
# SITEMAP
#########################################

# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
# FRONT_SITEMAP_ENABLED = False
# FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second


#########################################
# FEEDBACK
#########################################

# Note: See config in taiga-front too
# FEEDBACK_ENABLED = True
# FEEDBACK_EMAIL = "support@taiga.io"


#########################################
# STATS
#########################################

# STATS_ENABLED = False
# FRONT_SITEMAP_CACHE_TIMEOUT = 60*60  # In second


#########################################
# CELERY
#########################################
# Set to True to enable celery and work in async mode or False
# to disable it and work in sync mode. You can find the celery
# settings in settings/celery.py and settings/celery-local.py
CELERY_ENABLED = True

# Async
# see celery_local.py
RABBITMQ_USER = CONFIG['RABBITMQ_USER']
RABBITMQ_PASSWORD = CONFIG['RABBITMQ_PASSWORD']
RABBITMQ_VHOST = CONFIG['RABBITMQ_VHOST']
RABBITMQ_HOST = CONFIG['RABBITMQ_HOST']
RABBITMQ_PORT = CONFIG['RABBITMQ_PORT']
RABBITMQ_URL = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{RABBITMQ_VHOST}"
EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": RABBITMQ_URL}


#########################################
# IMPORTERS
#########################################

IMPORTERS = {}
# Configuration for the GitHub importer
# Remember to enable it in the front client too.
IMPORTERS["github"] = {
    "active": CONFIG['IMPORTER_GITHUB_ENABLED'],
    "client_id": GITHUB_API_CLIENT_ID,
    "client_secret": GITHUB_API_CLIENT_SECRET
}

# Configuration for the Trello importer
# Remember to enable it in the front client too.
IMPORTERS["trello"] = {
    "active": CONFIG['IMPORTER_TRELLO_ENABLED'],
    "api_key": CONFIG['TRELLO_API_KEY'],
    "secret_key": CONFIG['TRELLO_OAUTH_SECRET']
}

# Configuration for the Jira importer
# Remember to enable it in the front client too.
IMPORTERS["jira"] = {
    "active": CONFIG['IMPORTER_JIRA_ENABLED'],
    "consumer_key": CONFIG['JIRA_CONSUMER_KEY'],
    "cert": CONFIG['JIRA_CERT'],
    "pub_cert": CONFIG['JIRA_PUB_CERT'],
}

# Configuration for the Asane importer
# Remember to enable it in the front client too.
IMPORTERS["asana"] = {
    "active": CONFIG['IMPORTER_ASANA_ENABLED'],
    "callback_url": f"{FRONT_SCHEME}://{FRONT_DOMAIN}/project/new/import/asana",
    "app_id": CONFIG['ASANA_APP_ID'],
    "app_secret": CONFIG['ASANA_APP_SECRET'],
}
