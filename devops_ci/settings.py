#!/usr/bin/env python
#_*_ coding:utf-8 _*_

"""
Django settings for devops_ci project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from __future__ import absolute_import
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3a1zsy)l04rb@jsy7%b(8fa*d*pl4%)%&+b&(47a@v&cf@%bxy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]

# REST_FRAMEWORK = {
#     # 使用Django的标准`django.contrib.auth`权限管理类,
#     # 或者为尚未认证的用户，赋予只读权限.
#     'DEFAULT_PERMISSION_CLASSES': [
#           'rest_framework.permissions.AllowAny'
# #         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp',
    'rest_framework',
    'monitor_master',
    'djcelery',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'devops_ci.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'devops_ci.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
#     'slave': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'dcosauto',
#         'USER':'root',
#         'PASSWORD':'root',
#         'HOST':'192.168.10.1',
#         'PORT':'3306',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dcosauto',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'192.168.10.1',
        'PORT':'3306',
    }
}

'''
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    },
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

'''



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

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
# disable TZ
USE_TZ = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
import os


STATICFILES_DIRS = (
        os.path.join(BASE_DIR,"statics"),
                    )

TEMPLATES_DIRS = (
        os.path.join(BASE_DIR,"templates")
                  )

import djcelery        # 导入celery
djcelery.setup_loader()        #加载celery
BROKER_URL = 'redis://:root@192.168.10.3:6379/0'   # 配置clery的 broker（这里使用redis，官方推荐rabbitmq）
# BROKER_URL = 'redis://:密码@主机地址:端口号/数据库号'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
#计划任务
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERY_ENABLE_UTC = False # 不是用UTC
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_TASK_RESULT_EXPIRES = 10 #任务结果的时效时间