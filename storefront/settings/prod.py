import os
from .common import *


DEBUG = False
ALLOWED_HOSTS = ['www.rangvida.com']

SECRET_KEY = os.getenv('SECRET_KEY')