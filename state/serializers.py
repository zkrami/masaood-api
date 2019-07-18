from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import State
# Create your models here.


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        exclude = ("createdAt", )

