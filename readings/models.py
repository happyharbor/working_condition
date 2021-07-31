import datetime

from django.db import models
from django.utils import timezone


class Reading(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    reading_date = models.DateTimeField('date readings were measured')

    def was_red_recently(self):
        return self.reading_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return 'Temperature:{}, Humidity:{}'.format(self.temperature, self.humidity)
