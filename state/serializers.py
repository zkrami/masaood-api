from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import State
# Create your models here.
from center.serializers import CenterSerializer

class StateSerializer(ModelSerializer):

    centers = CenterSerializer(many=True , read_only=True)
    class Meta:
        model = State
        exclude = ("createdAt", )
        

