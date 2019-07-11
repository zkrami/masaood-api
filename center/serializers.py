from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import Center
# Create your models here.


class CenterSerializer(ModelSerializer):

    class Meta:
        model = Center
        exclude = ('createdAt',)
