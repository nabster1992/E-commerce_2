import os
from .common import *


DEBUG = False
ALLOWED_HOSTS = ['rangvida.com', 'www.rangvida.com']

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nhussainjee$storefront',
        'USER': 'nhussainjee',
        'PASSWORD': 'Swordking1!',
        'HOST': 'nhussainjee.mysql.pythonanywhere-services.com',
    }
}
    
