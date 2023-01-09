"""
Django settings for cestlavie_nataly project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7^rs=63zm&3$gp4ven9j6q9gy(#$0l*g#n69d9e%oa%0ete$3m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
		'blog',
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

ROOT_URLCONF = 'cestlavie_nataly.urls'

TEMPLATES = [
		{
				'BACKEND' : 'django.template.backends.django.DjangoTemplates',
				'DIRS'    : [
						os.path.join(BASE_DIR, 'templates'),
						],
				'APP_DIRS': True,
				'OPTIONS' : {
						'context_processors': [
								'django.template.context_processors.debug',
								'django.template.context_processors.request',
								'django.contrib.auth.context_processors.auth',
								'django.contrib.messages.context_processors.messages',
								],
						},
				},
		]

WSGI_APPLICATION = 'cestlavie_nataly.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
		'default': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME'  : BASE_DIR / 'db.sqlite3',
				}
		}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AWS_ACCESS_KEY_ID = 'YCAJEex1zWQPUlEP6wzwt3NSm'
AWS_SECRET_ACCESS_KEY = 'YCM832Yu_18vPCs2h1oGz4hTru4OO6o85ir1cof1'
AWS_DEFAULT_REGION = 'ru-central1'
ENDPOINT_URL = 'https://storage.yandexcloud.net'
BUCKET_NAME = 'cestlavie-nataly-storage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
