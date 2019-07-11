from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import AbstractProduct, Size, Grade, Product
from .serializers import AbstractProductSerializer, SizeSerializer, GradeSerializer, AbstractProductDetailSerializer, ProductSerializer, ProductDetailSerializer
from shared.mixins.per_action_serializer import PerActionSerializerMixin


class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = ()


class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = ()


class AbstractProductViewSet(PerActionSerializerMixin, ModelViewSet):
    queryset = AbstractProduct.objects.all()
    serializer_class = AbstractProductSerializer
    permission_classes = ()
    serializer_action_classes = {
        'list': AbstractProductDetailSerializer,
        'retrieve': AbstractProductDetailSerializer
    }


class ProductViewSet(PerActionSerializerMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = ()
    serializer_action_classes = {
        'list': ProductDetailSerializer,
        'retrieve': ProductDetailSerializer
    }
