from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .serializers import CenterSerializer, CenterDetailSerializer, CenterProductAdminSerializer, CenterProductDetailSerializer
from .models import Center, CenterProduct

from shared.permissions import IsAdminOrReadOnly

from shared.mixins.per_action_serializer import PerActionSerializerMixin
from center import filters 

class CenterViewSet(PerActionSerializerMixin, ModelViewSet):
    serializer_class = CenterSerializer
    permission_classes = (IsAdminOrReadOnly, )
    permission_classes = ()
    queryset = Center.objects.all()
    serializer_action_classes = {
        'list': CenterDetailSerializer,
        'retrieve': CenterDetailSerializer
    }


class CenterProductViewSet(PerActionSerializerMixin, ModelViewSet):
    permission_classes = (IsAdminOrReadOnly, )
    permission_classes = ()
    serializer_class = CenterProductAdminSerializer
    queryset = CenterProduct.objects.all() 
    serializer_action_classes = {
        'list': CenterProductDetailSerializer,
        'retrieve': CenterProductDetailSerializer
    }
    filter_class = filters.CenterProductFilter

