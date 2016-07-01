from django.db import models

# Create your models here.
from django.utils import timezone


class Insult(models.Model):
    phrase = models.TextField()
    pronunciation = models.TextField()
    language = models.CharField(max_length=255)
    translation = models.TextField()

    def __str__(self):
        return self.translation

class Day(models.Model):
    date = models.DateField(default=timezone.now, primary_key=True)
    insult = models.ForeignKey(Insult, related_name='days')

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')