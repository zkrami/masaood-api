from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.username 
    pass
