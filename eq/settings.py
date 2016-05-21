import djcelery
djcelery.setup_loader()

"""
Django settings for eq project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from celery.schedules import crontab
from datetime import timedelta
# from app_eq_1.tasks import example

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')9%&trtxa)9vda3u$8*oiw=&#e#2n0u(i_2wojhwl!xft65t8c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'app_eq_1',
    #
    'crispy_forms',
    'tastypie',
    'djsupervisor',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'djcelery',
    # 'tinymce',
     'redactor',

    # 'django.contrib.sites',
    # 'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'eq.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eq.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# ENV_PATH = os.path.abspath(os.path.dirname(__file__))
# MEDIA_ROOT = os.path.join(ENV_PATH, 'media/')
MEDIA_ROOT = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join("static/")
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    os.path.join(BASE_DIR, "app_eq_1", "static"),
    # '/var/www/static/',
)

# BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

BROKER_URL = "redis"
BROKER_BACKEND = "redis"
REDIS_PORT = 6379
REDIS_HOST = "redis"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}


CELERYBEAT_SCHEDULE = {
    # # Executes every 30 second
    # 'add-every-30-seconds': {
    #     'task': 'app_eq_1.tasks.example',
    #     'schedule': timedelta(seconds=30),
    #     # 'args': (16, ),
    # },
    # Executes everyday morning at 6:30 A.M
    'add-every-day-morning': {
        'task': 'app_eq_1.tasks.every_day',
        'schedule': crontab(hour=6, minute=30),
        # 'args': (16, 16),
    },
    # Executes every Tuesday morning at 1:30 A.M
    'add-every-monday-morning': {
        'task': 'app_eq_1.tasks.every_week',
        'schedule': crontab(hour=1, minute=30, day_of_week=1),
        # 'args': (16, 16),
    },
    # Executes every 2-th day of month morning at 3:30 A.M
    'add-every-month': {
        'task': 'app_eq_1.tasks.every_month',
        'schedule': crontab(hour=3, minute=30, day_of_month=2),
    },
}


# ACCOUNT_ACTIVATION_DAYS = 2
# EMAIL_HOST = 'localhost'
# DEFAULT_FROM_EMAIL = 'webmaster@localhost'
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
REGISTRATION_AUTO_LOGIN = True
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/profile/mysetting",
}

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.getenv('EQ_SMTP_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EQ_SMTP_PASS', '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'
CRISPY_TEMPLATE_PACK = 'bootstrap3'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',  # all messages
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['null', 'console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'app_eq_1': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}


SERVER_ENVIRONMENT = os.getenv('RUN_ENV', '')
if SERVER_ENVIRONMENT == 'PROD':
    from settings_prod import *