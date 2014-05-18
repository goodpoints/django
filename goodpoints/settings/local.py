"""
local development settings. it should not be checked into your code repository.
"""
from goodpoints.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('scott', 'scott.leonard@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'dev.db'),
    }
}

# ROOT_URLCONF = 'goodpoints.urls.local'
# WSGI_APPLICATION = 'goodpoints.wsgi.local.application'
