from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import Center, CenterProduct, Product
from state.models import State
from drf_writable_nested import WritableNestedModelSerializer


class CenterProductSerializer(ModelSerializer):

    productId = PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product")
    class Meta:
        model = CenterProduct
        exclude = ("createdAt", "center", "product")


class CenterSerializer(WritableNestedModelSerializer):

   # products = CenterProductSerializer(many=True)
    statesId = PrimaryKeyRelatedField(
        allow_empty=False, many=True, queryset=State.objects.all(), source="states")

    class Meta:
        model = Center
        exclude = ('createdAt', 'states')


class CenterProductAdminSerializer(ModelSerializer):

    productId = PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="product")
    centerId = PrimaryKeyRelatedField(
        queryset=Center.objects.all(), source="center")

    class Meta:
        model = CenterProduct
        exclude = ("createdAt", "center", "product")


class CenterProductDetailSerializer(ModelSerializer):
    class Meta:
        model = CenterProduct
        exclude = ("center", )
        depth = 3


class CenterDetailSerializer(ModelSerializer):
   # products = CenterProductDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Center
        exclude = ()
        depth = 1
