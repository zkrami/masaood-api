from django.db import models
# Create your models here.
from django.conf import settings


class Media(models.Model):

    file = models.FileField(upload_to=settings.MEDIA_ROOT)
    createdAt = models.DateTimeField(auto_now_add=True)
    type = models.CharField(default="image" , max_length=30) 
    def __str__(self):
        return self.file.url
