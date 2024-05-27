# Desactivar el modo depuración en producción.
DEBUG = True
# Direcciones permitidas en producción.
ALLOWED_HOSTS = ["172.25.4.111"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_base_datos',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '172.25.4.111',
        'PORT': '5432',
    }
}