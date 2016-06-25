from django.db import models

# Create your models here.

class Insult(models.Model):
    phrase = models.TextField()
    pronunciation = models.TextField()
    language = models.CharField(max_length=255)
    translation = models.TextField()

    def __str__(self):
        return self.phrase

class Day(models.Model):
    date = models.DateField(auto_now_add=True, primary_key=True)
    insult = models.ForeignKey(Insult, related_name='days')

    def __str__(self):
        return self.date