from django.db import models
from django.conf import settings
from user.models import User
from center.models import Center
from product.models import Product


class Order(models.Model):

    StatusChoices = (("pending", "pending"),
                     ("assigned", "assigned"),
                     ("canceled", "canceled"),
                     ("delivered", "delivered"))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    center = models.ForeignKey(Center, on_delete=models.SET_NULL, null=True)
    deliveryAddress = models.TextField(default='')
    deliveryLat = models.FloatField(default=0)
    devliveryLng = models.FloatField(default=0)

    # enums
    status = models.CharField(max_length=20, choices=StatusChoices)

    createdAt = models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='products')

    class Meta:
        unique_together = ('order', 'product',)
