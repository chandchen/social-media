"""
Django settings for Auth_System project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from decouple import config, Csv
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'upload_app',
    'blog',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'rest_framework',
    'api',
    'social_django',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Auth_System.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'Auth_System.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'index'

MEDIA_URL = '/upload_app/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'upload_app').replace('\\', '/')

LOGIN_URL = '/users/login/'

# SMTP SETTING
EMAIL_HOST = 'smtp.qq.com'
EMAIL_POST = 465
EMAIL_HOST_USER = '13205012@qq.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True

# CELERY
BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp://guest@localhost//'

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERYBEAT_SCHEDULE = {
    'greet-every-15-seconds': {
        'task': 'upload_app.tasks.greet_every_15_seconds',
        'schedule': timedelta(seconds=15),
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
}

SOCIAL_AUTH_URL_NAMESPACE = 'social'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'account.authentication.EmailAuthBackend',
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.qq.QQOAuth2',
    'social.backends.facebook.FacebookOAuth2',
)

SOCIAL_AUTH_LOGIN_URL = 'http://chand.com:8000/users/login/'
SOCIAL_AUTH_LOGIN_ERROR_URL = 'http://chand.com:8000/users/login/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://chand.com:8000/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = 'http://chand.com:8000/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = 'http://chand.com:8000/'

SOCIAL_AUTH_WEIBO_KEY = config('SOCIAL_AUTH_WEIBO_KEY')
SOCIAL_AUTH_WEIBO_SECRET = config('SOCIAL_AUTH_WEIBO_SECRET')

SOCIAL_AUTH_WEIBO_SCOPE = ['email']
SOCIAL_AUTH_WEIBO_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, first_name, last_name, name, email',
}

SOCIAL_AUTH_TWITTER_KEY = config('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = config('SOCIAL_AUTH_TWITTER_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_QQ_KEY = config('SOCIAL_AUTH_QQ_KEY')
SOCIAL_AUTH_QQ_SECRET = config('SOCIAL_AUTH_QQ_SECRET')

SOCIAL_AUTH_QQ_SCOPE = ['email']
SOCIAL_AUTH_QQ_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, first_name, last_name, name, email',
}

SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    # 'social_core.pipeline.user.get_username',
    'users.pipeline.get_username',
    'social_core.pipeline.user.create_user',
    'users.pipeline.save_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)

# SOCIAL_AUTH_QQ_USE_OPENID_AS_USERNAME = True

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'publish_actions']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, first_name, last_name, name, email',
}