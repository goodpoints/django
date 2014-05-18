"""
Base settings shared by all environments
"""
# import global settings to make it easier to extend settings
from django.conf.global_settings import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

# local time zone for this installation
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

# make this unique, and don't share it with anybody
SECRET_KEY = '3u0cgfq!i-!9#ubru*pi$y72*ey5_+i8_)byjn&he_&(r&bvt5'

INSTALLED_APPS = (
    #'goodpoints.apps.',
    'south',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

import os
import sys
import goodpoints as project_module

sys.path.insert(0, os.path.join(PROJECT_ROOT, "libs"))

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
PYTHON_BIN = os.path.dirname(sys.executable)

# 'activate_this.py' in the python bin/ means that we're running in a virtual environment
ve_path = os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR)))
if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
elif ve_path and os.path.exists(os.path.join(ve_path, 'bin', 'activate_this.py')):
    VAR_ROOT = os.path.join(ve_path, 'var')
else:
    VAR_ROOT = os.path.join(PROJECT_DIR, 'var')
if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

ROOT_URLCONF = 'goodpoints.urls'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
)

MIDDLEWARE_CLASSES += (
)

AUTHENTICATION_BACKENDS += (
)
