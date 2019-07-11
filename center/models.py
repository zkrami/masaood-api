from django.db import models
from django.conf import settings

import media.models


class Center(models.Model):
    nameEn = models.CharField(max_length=255)
    nameAr = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nameEn
