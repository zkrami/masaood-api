from django.db import models
from django.conf import settings
import media.models
from rest_framework.serializers import ModelSerializer


class Grade(models.Model):
    nameEn = models.CharField(max_length=255)
    nameAr = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nameEn


class Size(models.Model):
    nameAr = models.CharField(max_length=255)
    nameEn = models.CharField(max_length=255)
    code = models.CharField(max_length=255, default='')
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nameAr


class AbstractProduct(models.Model):

    GenderChoices = (
        ("female", "Female"),
        ("male", "Male")
    )

    nameEn = models.CharField(max_length=255)
    nameAr = models.CharField(max_length=255)
    descriptionAr = models.TextField(default='')
    descriptionEn = models.TextField(default='')

    images = models.ManyToManyField(media.models.Media)

    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    # enums
    gender = models.CharField(max_length=20, choices=GenderChoices)

    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nameEn


class Product(models.Model):

    StatusChoices = (("unavailable", "unavailable"),
                     ("available", "available"))
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=StatusChoices)
    price = models.DecimalField(default=0,  decimal_places=4, max_digits=10)

    abstractProduct = models.ForeignKey(
        AbstractProduct, on_delete=models.CASCADE, related_name="products")

    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.abstractProduct.nameAr + self.size.nameAr

    class Meta:
        unique_together = ('size', 'abstractProduct',)
