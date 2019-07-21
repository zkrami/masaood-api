from rest_framework.serializers import ModelSerializer
from .models import Media
# Create your models here.


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
    #todo
