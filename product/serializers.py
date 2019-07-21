from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField, ManyRelatedField
from .models import AbstractProduct, Grade, Size, Product
# Create your models here.

from media.models import Media


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        exclude = ("createdAt", )


class GradeSerializer(ModelSerializer):
    class Meta:
        model = Grade
        exclude = ("createdAt",)

class ProductSerializer(ModelSerializer):
    
    sizeId = PrimaryKeyRelatedField(queryset=Size.objects.all(), required=True , source="size")
    abstractProductId = PrimaryKeyRelatedField(label='AbstractProduct', queryset=AbstractProduct.objects.all(), required=True , source="abstractProduct")
    class Meta:
        model = Product
        exclude = ('createdAt', 'abstractProduct' , 'size')


class ProductDetailSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ('createdAt',)
        depth = 1


class AbstractProductDetailSerializer(ModelSerializer):
    products = ProductDetailSerializer(many=True, read_only=True)

    class Meta:
        model = AbstractProduct
        fields = "__all__"
        depth = 1


class AbstractProductSerializer(ModelSerializer):

    gradeId = PrimaryKeyRelatedField(queryset=Grade.objects.all() , source="grade")
    imagesId = PrimaryKeyRelatedField(
        allow_empty=False, many=True, queryset=Media.objects.all(), source="images")

    class Meta:
        model = AbstractProduct
        exclude = ('createdAt', 'grade', 'images')
