import os

# Desactivar el modo depuración en producción.
DEBUG = True
# Direcciones permitidas en producción.
ALLOWED_HOSTS = ["172.25.4.111"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '172.25.4.111',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')