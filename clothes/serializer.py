
from rest_framework import serializers
from .models import Cloth


class ClothSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cloth
        fields = ("name", "size", "create_date")
