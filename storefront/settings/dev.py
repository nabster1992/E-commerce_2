from .common import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = True




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'P@ssword'
    }
}