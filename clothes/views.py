from django.shortcuts import HttpResponse, Http404
from clothes.models import Cloth
# Create your views here.
from .serializer import ClothSerializer
from rest_framework import generics 
from django_filters.rest_framework import DjangoFilterBackend


class ClothAPI( generics.ListCreateAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
    permission_classes = ()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name' , 'size' , )

    