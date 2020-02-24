from django.db import models
from django.utils import timezone


class GPS(models.Model):
    created_at = models.DateTimeField()
    lat = models.FloatField()
    long = models.FloatField()
    updated_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.lat) + "," + str(self.long) + "," + str(self.created_at)
