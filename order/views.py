from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import Order, OrderProduct
from .serializers import OrderSerialier, OrderDetailSerialier, OrderProductSerializer
from shared.mixins.per_action_serializer import PerActionSerializerMixin
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response 
class OrderViewSet(PerActionSerializerMixin, ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerialier
    permission_classes = ()
    serializer_action_classes = {
        'list': OrderDetailSerialier,
        'retrieve': OrderDetailSerialier
    }

    def create(self, request, *args, **kwargs):
        
        request.data["user"] = request.user.id 
        
        return super().create(request , *args , **kwargs)
