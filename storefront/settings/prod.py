import os
from .common import *
from decouple import config


DEBUG = False
ALLOWED_HOSTS = ['rangvida.com', 'www.rangvida.com']

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nhussainjee$storefront',
        'USER': 'nhussainjee',
        'PASSWORD': 'Swordking1!',
        'HOST': 'nhussainjee.mysql.pythonanywhere-services.com',
        'PORT': '3306'
    }
}
    
