from django.db.models import Q

from django.utils import timezone
from django.utils.timezone import get_current_timezone
from django.views.generic import TemplateView
from exoticinsult.api import models



class InsultPageView(TemplateView):
    template_name = 'insult.html'

    def get_context_data(self, **kwargs):
        context = super(InsultPageView, self).get_context_data(**kwargs)
        date = kwargs.get('date', timezone.localtime(value=timezone.now(), timezone=get_current_timezone()).date())

        # we need to make sure the insult has have been displayed in the previous year, but because we are generating
        # data for past dates, we also need to make sure that the insult has not been used in the future year as well
        defaults = {'insult': models.Insult.objects.exclude(
                Q(days__date__range=[date - timezone.timedelta(days=365), date + timezone.timedelta(days=365)]) |
                Q(days__isnull=False)).order_by('?').first()}
        day, created = models.Day.objects.get_or_create(pk=date, defaults=defaults)
        context['insult'] = day.insult
        context['timezonetest'] = get_current_timezone()
        return context