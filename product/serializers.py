from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import AbstractProduct, Grade, Size, Product
# Create your models here.


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        execlude = ("createdAt", )
        fields = "__all__"


class GradeSerializer(ModelSerializer):
    class Meta:
        model = Grade
        execlude = ("createdAt",)
        fields = "__all__"




class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ('createdAt',)


class ProductDetailSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ('createdAt',)
        depth = 1



class AbstractProductDetailSerializer(ModelSerializer):
    products = ProductDetailSerializer(many=True , read_only=True)
    class Meta:
        model = AbstractProduct
        fields = "__all__"
        depth = 1


class AbstractProductSerializer(ModelSerializer):

    class Meta:
        model = AbstractProduct
        exclude = ('createdAt',)
