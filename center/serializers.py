from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import Center
from drf_writable_nested import WritableNestedModelSerializer

class CenterSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Center
        exclude = ('createdAt',)
