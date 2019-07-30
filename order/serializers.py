from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from rest_framework import serializers
from .models import Order, OrderProduct, StatusEnum
# Create your models here.
from center.models import Center
from drf_writable_nested import WritableNestedModelSerializer
from datetime import datetime


class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        exclude = ("createdAt", "order", )


class OrderSerialier(WritableNestedModelSerializer):
    # @todo
    # DeliverAddress and Lat Lang Adress
    # one of them required in case of absence of center

    products = OrderProductSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    centerId = PrimaryKeyRelatedField(
        queryset=Center.objects.all(), source="center", required=False)

    def create(self, validated_data):
    
        if "center" in validated_data:
            validated_data["status"] = StatusEnum.assigned.value
            validated_data["isDelivery"] = False
            validated_data["assignedAt"] = datetime.now()
        else:
            validated_data["isDelivery"] = True


        return super().create(validated_data)

    def validate(self, attrs):
        total = 0
        for orderProduct in attrs["products"]:
            total += orderProduct["count"] * orderProduct["product"].price

        if "center" not in attrs:
            total += 10 

        attrs["total"] = total
        return super().validate(attrs)

    class Meta:
        model = Order
        exclude = ('createdAt', 'assignedAt', 'deliveredAt',
                   'canceledAt',  'status', 'total' , 'isDelivery')


class OrderProductDetailSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        exclude = ("order", )
        depth = 2


class OrderDetailSerializer(ModelSerializer):
    products = OrderProductDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        depth = 2


class OrderAssignSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ("center",)

    def validate(self, attrs):
        attrs["status"] = StatusEnum.assigned.value
        attrs["assignedAt"] = datetime.now()

        return super().validate(attrs)


class OrderCancelSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ()

    def validate(self, attrs):
        attrs["status"] = StatusEnum.canceled.value
        attrs["canceledAt"] = datetime.now()
        return super().validate(attrs)


class OrderDeliveringSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ()

    def validate(self, attrs):
        attrs["status"] = StatusEnum.delivering.value 
        attrs["deliveringAt"] = datetime.now()
        return super().validate(attrs)


class OrderPackSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ()

    def validate(self, attrs):
        attrs["status"] = StatusEnum.packed.value 
        attrs["packedAt"] = datetime.now()
        return super().validate(attrs)



class OrderDeliverSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ()

    def validate(self, attrs):
        attrs["status"] = StatusEnum.delivered.value
        attrs["deliveredAt"] = datetime.now()
        return super().validate(attrs)
