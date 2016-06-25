from exoticinsult.settings import *

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

DEBUG=True