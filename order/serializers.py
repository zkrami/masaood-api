from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import Order, OrderProduct
# Create your models here.




class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        execlude = ("createdAt",)
        fields = "__all__"


class OrderSerialier(ModelSerializer):
    # @todo 
    # DeliverAddress and Lat Lang Adress 
    # one of them required in case of absence of center  
    products = OrderProductSerializer(many=True)
    class Meta:
        model = Order
        exclude = ('createdAt', 'status' , 'user' )


class OrderDetailSerialier(ModelSerializer):

    class Meta:
        model = Order
        exclude = ('createdAt',)
        depth = 1

