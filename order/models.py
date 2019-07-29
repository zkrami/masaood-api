from django.db import models
from django.conf import settings
from user.models import User
from center.models import Center
from product.models import Product
import enum


class StatusEnum(enum.Enum):
    pending = "pending"
    assigned = "assigned"
    canceled = "canceled"
    packed = "packed"
    inDelivery = "inDelivery"
    delivered = "delivered"

    def toChoices():
        return ((StatusEnum.pending.value, "pending"),
                (StatusEnum.assigned.value, "assigned"),
                (StatusEnum.canceled.value, "canceled"),
                (StatusEnum.inDelivery.value, "inDelivery"),
                (StatusEnum.packed.value, "packed"),
                (StatusEnum.delivered.value, "delivered"))


class Order(models.Model):

    StatusChoices = StatusEnum.toChoices()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    center = models.ForeignKey(Center, on_delete=models.SET_NULL, null=True)
    deliveryAddress = models.TextField(default='')
    deliveryLat = models.FloatField(default=0)
    devliveryLng = models.FloatField(default=0)
    total = models.DecimalField(decimal_places=4, max_digits=10)

    # enums
    status = models.CharField(
        max_length=20, choices=StatusChoices, default=StatusEnum.pending.value)

    createdAt = models.DateTimeField(auto_now_add=True)
    canceledAt = models.DateTimeField(null=True)
    deliveredAt = models.DateTimeField(null=True)
    assignedAt = models.DateTimeField(null=True)


class OrderProduct(models.Model):
    count = models.IntegerField()
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('order', 'product',)
