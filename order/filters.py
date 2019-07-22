from order import models 
import rest_framework_filters as filters


class OrderFilter(filters.FilterSet):

    class Meta:
        model = models.Order
        fields = {
            'user' : "__all__" , 
            'center' : "__all__" , 
            'deliveryAddress' : "__all__" , 
            'deliveryLat' : "__all__" , 
            'devliveryLng' : "__all__" , 
            'total' : "__all__" , 
            'status' : "__all__" , 
            'createdAt' : "__all__" , 
            'canceledAt' : "__all__" , 
            'deliveredAt' : "__all__" , 
            'assignedAt' : "__all__" , 
        }

