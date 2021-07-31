import os

from server.settings.common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'readings',
        'USER': 'pi',
        'PASSWORD': os.environ['WORK_RATE_DB_PASS'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
