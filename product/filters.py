from product import models
import rest_framework_filters as filters


class AbstractProductFilter(filters.FilterSet):
    nameEn = filters.AllLookupsFilter()

    class Meta:
        model = models.AbstractProduct
        fields = {
        }


class ProductFilter(filters.FilterSet):

    class Meta:
        model = models.Product
        fields = {
            'abstractProduct' : '__all__'
        }
