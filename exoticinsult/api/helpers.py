from django.db.models import Q
from django.utils import timezone
from exoticinsult.api import models


def get_insult(date):
    """Get an insult from the database"""
    # attempt to retrieve and insult that has not been used previously, and because we are generating insults
    # for past dates, make sure it has not been used in the future year as well.
    insult = models.Insult.objects.exclude(
        Q(days__date__range=[date - timezone.timedelta(days=365), date + timezone.timedelta(days=365)]) |
        Q(days__isnull=False)).order_by('?').first()
    # if we can't get an insult we haven't used, we need to get some insult. Random ordering is not the fastest,
    # but once our database is big enough to hinder performance, we can remove this code entirely.
    if not insult:
        insult = models.Insult.objects.order_by('?').first()
    return insult