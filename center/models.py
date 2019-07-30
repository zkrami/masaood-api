from django.db import models
from django.conf import settings
from state.models import State
import media.models
from product.models import Product
import enum
# Create your models here.


class StatusEnum(enum.Enum):
    activated = "activated"
    deactivated = "deactivated"

    def toChoices():
        return ((StatusEnum.activated.value, "activated"),
                (StatusEnum.deactivated.value, "deactivated"))


class Center(models.Model):
    nameEn = models.CharField(max_length=255)
    nameAr = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    status = models.CharField(
        max_length=100, default=StatusEnum.activated.value, choices=StatusEnum.toChoices())
    createdAt = models.DateTimeField(auto_now_add=True)
    states = models.ManyToManyField(State, related_name="centers")
   

    def __str__(self):
        return self.nameEn


class CenterProduct(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE , related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    class Meta:
        unique_together = ('center', 'product',)
