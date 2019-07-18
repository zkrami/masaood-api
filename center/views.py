from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .serializers import CenterSerializer
from .models import Center

from shared.permissions import IsAdminOrReadOnly


class CenterViewSet(ModelViewSet):
    serializer_class = CenterSerializer
    permission_classes = (IsAdminOrReadOnly, )
    permission_classes = () 
    queryset = Center.objects.all()
