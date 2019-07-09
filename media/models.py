from django.db import models
# Create your models here.
from django.conf import settings

class Media(models.Model):

    file = models.FileField(upload_to=settings.MEDIA_ROOT)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file
