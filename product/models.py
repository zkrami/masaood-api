from django.db import models
from django.conf import settings
import media.models
from rest_framework.serializers import ModelSerializer


class Grade(models.Model):
    nameEn = models.CharField(max_length=255)
    nameAr = models.CharField(max_length=255)
    code = models.CharField(max_length=20, default='', unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nameEn


class Size(models.Model):
    nameAr = models.CharField(max_length=255)
    nameEn = models.CharField(max_length=255)
    code = models.CharField(max_length=20, default='', unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nameAr


class AbstractProductManager(models.Manager):
    
    def delete(self):
        # todo implement delete 
        pass 
        
    def create(self, **kwargs):    
        kwargs["order"] = self.count() + 1
        return super().create(**kwargs)

    
    def batch_order(self , batch):

        for obj in batch: 
            self.filter(pk=obj["id"]).update(order=obj["order"])
        

    def set_order(self, instance , order):        
        if instance.order == order:
            return

        prev_order = instance.order 

       
     
        if prev_order > order :        
            self.filter(order__gte=order , order__lte=prev_order).update(order=models.F('order') + 1)
        else:
            self.filter(order__gte=prev_order , order__lte=order).update(order=models.F('order') - 1)

        instance.order = order
        instance.save()

class AbstractProduct(models.Model):

    GenderChoices = (
        ("female", "Female"),
        ("male", "Male")
    )
    objects = AbstractProductManager()

    StatusChoices = (("unavailable", "unavailable"),
                     ("available", "available"))
    nameEn = models.CharField(max_length=255)
    nameAr = models.CharField(max_length=255)
    order = models.IntegerField(default=None, null=True)
    descriptionAr = models.TextField(default='')
    descriptionEn = models.TextField(default='')

    status = models.CharField(max_length=20, choices=StatusChoices, default="available")


    images = models.ManyToManyField(media.models.Media)

    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    # enums
    gender = models.CharField(max_length=20, choices=GenderChoices)

    createdAt = models.DateTimeField(auto_now_add=True)
  


    def __str__(self):
        return self.nameEn


class Product(models.Model):

    StatusChoices = (("unavailable", "unavailable"),
                     ("available", "available"))
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20, choices=StatusChoices, default="available")
    price = models.DecimalField(default=0,  decimal_places=4, max_digits=10)

    abstractProduct = models.ForeignKey(
        AbstractProduct, on_delete=models.CASCADE, related_name="products")

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.abstractProduct.nameAr + self.size.nameAr

    class Meta:
        unique_together = ('size', 'abstractProduct',)
