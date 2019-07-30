from django.db import models
from django.contrib.admin import ModelAdmin
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
import enum
# Create your models here.
import rest_framework
from center.models import Center


class StatusEnum(enum.Enum):
    activated = "activated"
    deactivated = "deactivated"

    def toChoices():
        return ((StatusEnum.activated.value, "activated"),
                (StatusEnum.deactivated.value, "deactivated"))


class User(AbstractUser):
    mobile = models.CharField(
        max_length=255, null=True, unique=True, default=None)
    USERNAME_FIELD = 'mobile'
    username = models.CharField(
        max_length=150,
        unique=False,
        default=''
    )
    verified = models.BooleanField(default=False)
    email = models.EmailField(null=True, unique=True, default=None)
    password = models.CharField(
        'password', max_length=128, null=True, default=None)

    status = models.CharField(
        max_length=100, default=StatusEnum.activated.value, choices=StatusEnum.toChoices())
    search_fields = ('id', )
    autocomplete_fields = ('id', )
    center = models.ForeignKey(Center, on_delete=models.SET_NULL, null=True)

    def clean(self):
        if self.email is None and self.mobile is None:
            raise ValidationError('email and mobile are both None')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)


class UserAdmin(ModelAdmin):
    search_fields = ("mobile", )
    pass
