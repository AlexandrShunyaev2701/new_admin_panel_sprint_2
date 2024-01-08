from example.settings import env


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.str('POSTGRES_PORT'),
        'OPTIONS': {
            'options': '-c search_path=public,content'
        }
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
