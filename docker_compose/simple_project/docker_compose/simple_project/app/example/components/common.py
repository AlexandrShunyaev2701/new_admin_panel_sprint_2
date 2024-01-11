from pathlib import Path

from example.settings import env

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env.str('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
ROOT_URLCONF = 'example.urls'
WSGI_APPLICATION = 'example.wsgi.application'
ASGI_APPLICATION = 'example.asgi.application'
