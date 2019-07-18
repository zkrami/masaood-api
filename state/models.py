from django.db import models

# Create your models here.


class State(models.Model):
    nameEn = models.CharField(max_length=255)
    nameAr = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nameEn