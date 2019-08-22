from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import AbstractProduct, Size, Grade, Product
from .serializers import AbstractProductSerializer, SizeSerializer, GradeSerializer, AbstractProductDetailSerializer, ProductSerializer, ProductDetailSerializer, AbstractProductOrderSerializer, AbstractProductBatchOrderSerializer
from shared.mixins.per_action_serializer import PerActionSerializerMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from shared.permissions import IsAdminOrReadOnly
from product import filters
from rest_framework.decorators import action
from rest_framework.response import Response


class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = (IsAdminOrReadOnly, )


class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = (IsAdminOrReadOnly, )


class AbstractProductViewSet(PerActionSerializerMixin, ModelViewSet):
    queryset = AbstractProduct.objects.all()
    serializer_class = AbstractProductSerializer
    permission_classes = ()  # @todo permissoins
    serializer_action_classes = {
        'list': AbstractProductDetailSerializer,
        'retrieve': AbstractProductDetailSerializer,
        'order': AbstractProductOrderSerializer,
        'batch_order': AbstractProductBatchOrderSerializer
    }
    filter_class = filters.AbstractProductFilter

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="user").count() == 1:
            return AbstractProduct.objects.filter(status="available")
        return AbstractProduct.objects.all()

    @action(detail=False, methods=['put'], url_path="batch-order")
    def batch_order(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, many=True, partial=True)
        serializer.is_valid(raise_exception=True)

        manager = AbstractProduct.objects
        manager.batch_order(request.data)

        return Response({'message': 'changed'})

    @action(detail=True, methods=['put'])
    def order(self, request, pk=None):

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        manager = AbstractProduct.objects
        order = request.data["order"]
        manager.set_order(instance, order)

        return Response({'message': 'changed'})

    # ["nameEn" , "nameAr" , "descriptionAr" , "descriptionEn" , "code" , "image" , "grade" , "price" , "gender" , "status" , "createdAt"]


class ProductViewSet(PerActionSerializerMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = ()  # @todo permissoins

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="user").count() == 1:
            return Product.objects.filter(status="available")
        return Product.objects.all()

    serializer_action_classes = {
        'list': ProductDetailSerializer,
        'retrieve': ProductDetailSerializer
    }
    filter_class = filters.ProductFilter
