from django.db import models
from django.contrib.admin import ModelAdmin

from django.contrib.auth.models import AbstractUser
# Create your models here.
import rest_framework


class User(AbstractUser):
    mobile = models.CharField(max_length=255, unique=True)
    USERNAME_FIELD = 'mobile'
    username = models.CharField(
        max_length=150,
        unique=False,
        default=''
    )
    verified = models.BooleanField(default=False)
    search_fields = ('id', )
    autocomplete_fields = ('id', )

    def __str__(self):
        return self.username
    pass


class UserAdmin(ModelAdmin):
    search_fields = ("mobile" , ) 
    pass 
