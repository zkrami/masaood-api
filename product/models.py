from django.db import models
from django.conf import settings

import media.models


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


class AbstractProduct(models.Model):

    GenderChoices = (
        ("female", "Female"),
        ("male", "Male")
    )
    StatusChoices = (("unavailable", "unavailable"),
                     ("available", "available"))

    nameEn = models.CharField(max_length=255)
    nameAr = models.CharField(max_length=255)
    descriptionAr = models.TextField(default='')
    descriptionEn = models.TextField(default='')
    code = models.CharField(max_length=255)
    image = models.ForeignKey(
        media.models.Media, on_delete=models.SET_NULL, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    price = models.DecimalField(default=0,  decimal_places=4, max_digits=10)

    # enums
    gender = models.CharField(max_length=20, choices=GenderChoices)
    status = models.CharField(max_length=20, choices=StatusChoices)

    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nameEn
