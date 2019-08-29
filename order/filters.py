from order import models
import rest_framework_filters as filters
from user.filters import UserFilter
from user.models import User


class OrderFilter(filters.FilterSet):
    user = filters.RelatedFilter(UserFilter, field_name='user', queryset=User.objects.all())

    class Meta:
        model = models.Order
        fields = {
            'center': "__all__",
            'deliveryAddress': "__all__",
            'deliveryLat': "__all__",
            'devliveryLng': "__all__",
            'total': "__all__",
            'status': "__all__",
            'createdAt': "__all__",
            'canceledAt': "__all__",
            'deliveredAt': "__all__",
            'assignedAt': "__all__",
            'deleted': "__all__",
            'archived': "__all__"
        }
