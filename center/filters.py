from center import models
import rest_framework_filters as filters


class CenterProductFilter(filters.FilterSet):

    class Meta:
        model = models.CenterProduct
        fields = {
            'count': "__all__",
            'center': "__all__",
            'product': "__all__",
        }
