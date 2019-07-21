from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import Center
from state.models import State

class CenterSerializer(ModelSerializer):

    statesId = PrimaryKeyRelatedField(
        allow_empty=False, many=True, queryset=State.objects.all(), source="states")

    class Meta:
        model = Center
        exclude = ('createdAt','states')



class CenterDetailSerializer(ModelSerializer):
    class Meta:
        model=Center
        exclude = ('createdAt',)
        depth = 1 

