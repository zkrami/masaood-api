from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField, ManyRelatedField, ListSerializer, ValidationError
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

    sizeId = PrimaryKeyRelatedField(
        queryset=Size.objects.all(), required=True, source="size")
    abstractProductId = PrimaryKeyRelatedField(
        label='AbstractProduct', queryset=AbstractProduct.objects.all(), required=True, source="abstractProduct")

    class Meta:
        model = Product
        exclude = ('createdAt', 'abstractProduct', 'size')


class ProductDetailListSerializer(ListSerializer):

    def to_representation(self, data):

        user = self.context['request'].user
        if user.groups.filter(name="user").count() == 1:
            data = data.filter(status="available")
        return super().to_representation(data)


class ProductDetailSerializer(ModelSerializer):

    class Meta:
        model = Product
        list_serializer_class = ProductDetailListSerializer
        exclude = ('createdAt',)
        depth = 1


class AbstractProductDetailSerializer(ModelSerializer):
    products = ProductDetailSerializer(many=True, read_only=True)

    class Meta:
        model = AbstractProduct
        fields = "__all__"
        depth = 1


class AbstractProductSerializer(ModelSerializer):

    gradeId = PrimaryKeyRelatedField(
        queryset=Grade.objects.all(), source="grade")
    imagesId = PrimaryKeyRelatedField(
        allow_empty=False, many=True, queryset=Media.objects.all(), source="images")

    class Meta:
        model = AbstractProduct
        exclude = ('createdAt', 'grade', 'images', 'order')


class AbstractProductOrderSerializer(ModelSerializer):
     def validate(self, attrs):
        order = attrs["order"]

        if order <= 0 or order > AbstractProduct.objects.count():
            raise ValidationError(
                {"order": "order must be in range of [1 , number of products]"}, "ORDER_VALIDATION_ERROR")

        return attrs 

     class Meta:
        model = AbstractProduct
        fields = ("order" , )



class AbstractProductBatchOrderSerializer(ModelSerializer):
     def validate(self, attrs):
        order = attrs["order"]

        if order <= 0 or order > AbstractProduct.objects.count():
            raise ValidationError(
                {"order": "order must be in range of [1 , number of products]"}, "ORDER_VALIDATION_ERROR")

        return super().validate(attrs)  

     class Meta:
        model = AbstractProduct
        fields = ("order" , )