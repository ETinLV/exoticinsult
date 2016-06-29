from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.utils.timezone import localtime, now
from django.views.generic import TemplateView
from exoticinsult.api import models
from exoticinsult.api.helpers import get_insult
from django.conf import settings
class InsultPageView(TemplateView):
    template_name = 'insult.html'

    def get_context_data(self, **kwargs):
        context = super(InsultPageView, self).get_context_data(**kwargs)
        # This is not quite right, as currently we are not getting the user's timezone. Once the frontend is converted
        # to angular, we can get the client date from the frontend.
        date = self.request.GET.get('date')
        if date:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        else:
            date = localtime(now()).date()

        # We need an insult in case we need to create the day. We could use a try/except to only get the insult if their
        # is not a day, but this is cleaner and should not slow anything down.
        defaults = {'insult': get_insult(date)}
        day, created = models.Day.objects.get_or_create(pk=date, defaults=defaults)
        context['insult'] = day.insult
        context['day'] = day
        return context