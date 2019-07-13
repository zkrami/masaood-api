from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from rest_framework import serializers
from .models import Order, OrderProduct
# Create your models here.

from drf_writable_nested import WritableNestedModelSerializer


class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        exclude = ("createdAt", "order", )


class OrderSerialier(WritableNestedModelSerializer):
    # @todo
    # DeliverAddress and Lat Lang Adress
    # one of them required in case of absence of center

    products = OrderProductSerializer(many=True)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        exclude = ('createdAt', 'status')


class OrderDetailSerialier(ModelSerializer):
    products = OrderProductSerializer(many=True , read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        depth = 1
