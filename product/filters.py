from product import models 
import rest_framework_filters as filters

class AbstractProductFilter(filters.FilterSet):
   # price = filters.AllLookupsFilter()
    class Meta:
        model = models.AbstractProduct
        fields = {
        }

