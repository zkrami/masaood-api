from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from .models import Order, OrderProduct, StatusEnum
from .serializers import OrderSerialier, OrderDetailSerializer, OrderProductSerializer, OrderAssignSerializer , OrderDeliverSerializer , OrderCancelSerializer 
from shared.mixins.per_action_serializer import PerActionSerializerMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from shared.permissions import IsOwner
from rest_framework.decorators import action
from rest_framework.response import Response
from order import filters 

# todo prevent edit
class OrderViewSet(PerActionSerializerMixin, ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerialier
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_action_classes = {
        'list': OrderDetailSerializer,
        'retrieve': OrderDetailSerializer
    }

    def get_queryset(self, *args, **kwargs):
        return Order.objects.all().filter(user=self.request.user)


class OrderAdminViewSet(PerActionSerializerMixin, ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerialier
    permission_classes = (IsAuthenticated, IsAdminUser)
    permission_classes = () 
    filter_class = filters.OrderFilter

    serializer_action_classes = {
        'list': OrderDetailSerializer,
        'retrieve': OrderDetailSerializer,
        'assign': OrderAssignSerializer , 
        'cancel' : OrderCancelSerializer , 
        'deliver' : OrderDeliverSerializer
    }

    @action(detail=True, methods=['put'])
    def assign(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def cancel(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def deliver(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data)
