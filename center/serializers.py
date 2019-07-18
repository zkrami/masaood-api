from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import Center

class CenterSerializer(ModelSerializer):
    class Meta:
        model = Center
        exclude = ('createdAt',)



class CenterDetailSerializer(ModelSerializer):
    class Meta:
        model=Center
        exclude = ('createdAt',)
        depth = 1 

