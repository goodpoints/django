"""
AWS production settings
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
      'ENGINE': 'django.db.backends.mysql',
      'NAME': os.environ['RDS_DB_NAME'],
      'USER': os.environ['RDS_USERNAME'],
      'PASSWORD': os.environ['RDS_PASSWORD'],
      'HOST': os.environ['RDS_HOSTNAME'],
      'PORT': os.environ['RDS_PORT'],
   }
}

# ROOT_URLCONF = 'goodpoints.urls.local'
# WSGI_APPLICATION = 'goodpoints.wsgi.local.application'
