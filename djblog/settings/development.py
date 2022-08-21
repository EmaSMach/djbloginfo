import dj_database_url

from .base import *


ALLOWED_HOSTS = ['*']

# configuración para usar postgres, vamos a leer la url de la variable de entorno
# DATABASE_URL que nos proporciona heroku

DATABASE_URL = os.getenv('DATABASE_URL')

# y eso lo usamos con dj_database_url para que lea los datos necesarios de la url
DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)
