from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import AbstractProduct, Grade, Size
# Create your models here.


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        execlude = ("createdAt", )
        fields = "__all__"


class GradeSerializer(ModelSerializer):
    class Meta:
        model = Grade
        execlude = ("createdAt",)
        fields = "__all__"


class AbstractProductSerializer(ModelSerializer):

    class Meta:
        model = AbstractProduct
        exclude = ('createdAt',)
        depth = 1
