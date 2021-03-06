from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from .models import Order, OrderProduct, StatusEnum
from .serializers import OrderSerialier, OrderDetailSerializer, OrderProductSerializer, OrderAssignSerializer, OrderDeliverSerializer, OrderCancelSerializer, OrderPackSerializer, OrderDeliveringSerializer, OrderArchiveSerializer, OrderDeleteSerializer
from shared.mixins.per_action_serializer import PerActionSerializerMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from shared.permissions import IsOwner
from rest_framework.decorators import action
from rest_framework.response import Response
from order import filters, errors
from django.core.exceptions import ObjectDoesNotExist
from io import BytesIO , StringIO
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.http import HttpResponse


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
        'assign': OrderAssignSerializer,
        'cancel': OrderCancelSerializer,
        'deliver': OrderDeliverSerializer,
        'pack': OrderPackSerializer,
        'delivering': OrderDeliveringSerializer,
        'destroy': OrderDeleteSerializer,
        'archive': OrderArchiveSerializer
    }

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'deleted'})

    @action(detail=True, methods=['put'])
    def assign(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'assigned'})

    @action(detail=True, methods=['put'])
    def archive(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'archived'})

    @action(detail=True, methods=['put'])
    def cancel(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'canceled'})

    @action(detail=True, methods=['put'])
    def deliver(self, request, pk=None):
        order = self.get_object()
        if order.center is None:
            raise errors.OrderIsNotAssigned()

        if order.status is StatusEnum.delivered.value:
            raise errors.OrderIsDelivered()

        centerProducts = list()
        for orderProduct in order.products.all():
            try:
                centerProduct = order.center.products.get(
                    product_id=orderProduct.product_id)
                centerProduct.count -= orderProduct.count
                centerProducts.append(centerProduct)
            except ObjectDoesNotExist:
                raise errors.CenterHasNoProduct

        for centerProduct in centerProducts:
            centerProduct.save()

        serializer = self.get_serializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'message': 'delivered'})

    @action(detail=True, methods=['put'])
    def pack(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'message': 'packed'})

    @action(detail=True, methods=['put'])
    def delivering(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'message': 'delivering'})
    
    @action(detail=True , methods=['get'])
    def print(self,  request , pk=None):
        instance = self.get_object()
        template = get_template("order/invoice.html")
        html  = template.render({"order": instance})
        result = BytesIO()
        
        pdf = pisa.pisaDocument(html.encode("UTF-8") , dest=result )        
        if not pdf.err:            
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return HttpResponse('We had some errors' , 400 )
        



