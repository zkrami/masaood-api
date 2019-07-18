from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .serializers import StateSerializer
from .models import State
from shared.permissions import IsAdminOrReadOnly


class StateViewSet(ModelViewSet):
    serializer_class = StateSerializer
    permission_classes = (IsAdminOrReadOnly, )
    permission_classes = ()
    queryset = State.objects.all() 
