from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .serializers import CenterSerializer , CenterDetailSerializer
from .models import Center

from shared.permissions import IsAdminOrReadOnly

from shared.mixins.per_action_serializer import PerActionSerializerMixin


class CenterViewSet(PerActionSerializerMixin, ModelViewSet):
    serializer_class = CenterSerializer
    permission_classes = (IsAdminOrReadOnly, )
    permission_classes = ()
    queryset = Center.objects.all()
    serializer_action_classes = {
        'list': CenterDetailSerializer,
        'retrieve': CenterDetailSerializer
    }
