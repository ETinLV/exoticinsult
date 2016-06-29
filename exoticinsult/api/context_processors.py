from django.conf import settings


def show_google_analytics(request):
    if settings.DEBUG:
        return {'analytics': False}
    else:
        return {'analytics': True}