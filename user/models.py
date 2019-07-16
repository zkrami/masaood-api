from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=255, unique=True)
    USERNAME_FIELD = 'mobile'
    username = models.CharField(
        max_length=150,
        unique=False,
        default=''
    )
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    pass
