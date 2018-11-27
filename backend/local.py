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

# ADMINS = (
#    ("Admin", "example@example.com"),
# )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST', default='postgresql'),
        'PORT': env('POSTGRES_PORT', default=5432),
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
#REST_FRAMEWORK["DEFAULT_THROTTLE_WHITELIST"] = []


#########################################
# MAIL SYSTEM SETTINGS (Default setup GMAIL)
#########################################

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = env('EMAIL_FROM_DEFAULT', default='john@doe.com')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', cast=bool, default=True)
# You cannot use both (TLS and SSL) at the same time!
EMAIL_USE_SSL = env('EMAIL_USE_SSL', cast=bool, default=False)
EMAIL_HOST = env('EMAIL_USE_SSL', default='smtp.gmail.com')
EMAIL_PORT = env('EMAIL_PORT', default=587)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='youremail@gmail.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='yourpassword')

#########################################
# REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = env(
    'PUBLIC_REGISTER_ENABLED', cast=bool, default=True)

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
USER_EMAIL_ALLOWED_DOMAINS = env('USER_EMAIL_ALLOWED_DOMAINS', default=None)

# PUCLIC OR PRIVATE NUMBER OF PROJECT PER USER
# MAX_PRIVATE_PROJECTS_PER_USER = None # None == no limit
# MAX_PUBLIC_PROJECTS_PER_USER = None # None == no limit
# MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None # None == no limit
# MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None # None == no limit

# GITHUB SETTINGS
GITHUB_URL = env('GITHUB_URL')
GITHUB_API_URL = env('GITHUB_API_URL')
GITHUB_API_CLIENT_ID = env('GITHUB_API_CLIENT_ID')
GITHUB_API_CLIENT_SECRET = env('GITHUB_API_CLIENT_SECRET')


#########################################
# SITEMAP
#########################################

# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
#FRONT_SITEMAP_ENABLED = False
# FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second


#########################################
# FEEDBACK
#########################################

# Note: See config in taiga-front too
#FEEDBACK_ENABLED = True
#FEEDBACK_EMAIL = "support@taiga.io"


#########################################
# STATS
#########################################

#STATS_ENABLED = False
# FRONT_SITEMAP_CACHE_TIMEOUT = 60*60  # In second


#########################################
# CELERY
#########################################
# Set to True to enable celery and work in async mode or False
# to disable it and work in sync mode. You can find the celery
# settings in settings/celery.py and settings/celery-local.py
CELERY_ENABLED = True


#########################################
# IMPORTERS
#########################################

IMPORTERS = {}
# Configuration for the GitHub importer
# Remember to enable it in the front client too.
IMPORTERS["github"] = {
    "active": env('IMPORTER_GITHUB_ENABLED', cast=bool, default=False),
    "client_id": env('GITHUB_API_CLIENT_ID'),
    "client_secret": env('GITHUB_API_CLIENT_SECRET')
}

# Configuration for the Trello importer
# Remember to enable it in the front client too.
IMPORTERS["trello"] = {
    "active": env('IMPORTER_TRELLO_ENABLED', cast=bool, default=False),
    "api_key": env('TRELLO_API_KEY'),
    "secret_key": env('TRELLO_OAUTH_SECRET')
}

# Configuration for the Jira importer
# Remember to enable it in the front client too.
IMPORTERS["jira"] = {
    "active": env('IMPORTER_JIRA_ENABLED', cast=bool, default=False),
    "consumer_key": env('JIRA_CONSUMER_KEY'),
    "cert": env('JIRA_CERT'),
    "pub_cert": env('JIRA_PUB_CERT'),
}

# Configuration for the Asane importer
# Remember to enable it in the front client too.
IMPORTERS["asana"] = {
    "active": env('IMPORTER_ASANA_ENABLED', cast=bool, default=False),
    "callback_url": "{}://{}/project/new/import/asana".format(SITES["front"]["scheme"],
                                                              SITES["front"]["domain"]),
    "app_id": env('ASANA_APP_ID'),
    "app_secret": env('ASANA_APP_SECRET'),
}
