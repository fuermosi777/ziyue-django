"""
Django settings for ziyue project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ul@vi$!-cv+(%0c@@_c2j+!5bv-38#y)sh!o6!=b=1o1mnghlp'

# SECURITY WARNING: don't run with debug turned on in production!
try:
    import local
    DEBUG = True
    SITE_ID = 3
except:
    DEBUG = False
    SITE_ID = 2

if not DEBUG:
    CACHE_BACKEND = 'memcached://127.0.0.1:30145/?timeout=900'
else:
    CACHE_BACKEND = 'dummy:///'

INTERNAL_IPS = (
    '127.0.0.1',
)

ALLOWED_HOSTS = [
    '*',
]

if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
else:
    CORS_ORIGIN_ALLOW_ALL = False


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
    'api',
    'log',
    'storages',
    'imagekit',
    'corsheaders',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware', # cache start
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', # cache end
)

ROOT_URLCONF = 'ziyue.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates/"),
        ],
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

WSGI_APPLICATION = 'ziyue.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'ziyue_db',
         'USER': 'fuermosi777',
         'PASSWORD': 'lh14589123',
         'HOST': 'ziyuedb.clansbmy63wh.ap-southeast-1.rds.amazonaws.com',
         'PORT': '5432',
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

# STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# AWS S3

AWS_STORAGE_BUCKET_NAME = 'ziyue'
AWS_ACCESS_KEY_ID = 'AKIAI2DIWAMCXA4I5VJA'
AWS_SECRET_ACCESS_KEY = '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'

STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_ROOT = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/media/'
MEDIA_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/media/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

AWS_QUERYSTRING_AUTH = False