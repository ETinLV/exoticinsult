import newrelic as newrelic

from exoticinsult.settings import *

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = [
    '.exoticinsultoftheday.com'
]
DEBUG=False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'