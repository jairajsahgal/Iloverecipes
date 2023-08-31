import os
from pathlib import Path
import django_heroku
import dj_database_url
from decouple import config
import boto3


import json

from django.core.exceptions import ImproperlyConfigured




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#
DB_PASSWORD= os.environ.get('DB_PASSWORD')
NAME= os.environ.get('NAME')
DB_USER= os.environ.get('DB_USER')
SECRET_KEY=os.environ.get('SECRET_KEY')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY =os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME =os.environ.get('S3_BUCKET')


COMPRESS_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

COMPRESS_URL = 'https://d17usxoyp786nd.cloudfront.net'

# Use S3 for static files storage

STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/'
#STATIC_URL = '/static/'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Use S3 for media files storage

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#s3://iloverecipes/book_covers/Image.png

#https://iloverecipes.s3.us-east-2.amazonaws.com/book_covers/Image.png
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.us-east-2.amazonaws.com/media/'
# Media files (Uploaded files)
#MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'recipes', 'static','recipes')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'recipes')



DEBUG = True



ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'recipes',
  #  'recipes.apps.RecipesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FoodBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'recipes', 'templates', 'recipes')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]


WSGI_APPLICATION = 'FoodBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': NAME,
#        'USER': DB_USER,
#        'PASSWORD': DB_PASSWORD,
#        'HOST': '127.0.0.1',
#        'PORT': '3306',
#        'OPTIONS': {
#            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#        }
#
#    }
#}


DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        } 
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


MEDIA_URL_FROM_HOME= '../media/'


MEDIA_ROOT = os.path.join(BASE_DIR,'recipes','media')
print(MEDIA_ROOT)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())