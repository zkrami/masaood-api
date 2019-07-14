from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import User
# Create your models here.


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name" , "email" )




class AdminUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
