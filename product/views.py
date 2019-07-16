from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import AbstractProduct, Size, Grade, Product
from .serializers import AbstractProductSerializer, SizeSerializer, GradeSerializer, AbstractProductDetailSerializer, ProductSerializer, ProductDetailSerializer
from shared.mixins.per_action_serializer import PerActionSerializerMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from shared.permissions  import IsAdminOrReadOnly 
import rest_framework_filters as filters 

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
    permission_classes = ()
    serializer_action_classes = {
        'list': AbstractProductDetailSerializer,
        'retrieve': AbstractProductDetailSerializer
    }
   # filter_class = filters.AllValuesFilter
    #["nameEn" , "nameAr" , "descriptionAr" , "descriptionEn" , "code" , "image" , "grade" , "price" , "gender" , "status" , "createdAt"]



class ProductViewSet(PerActionSerializerMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = ( ) # @todo 
    serializer_action_classes = {
        'list': ProductDetailSerializer,
        'retrieve': ProductDetailSerializer
    }
