from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField
from .models import User
# Create your models here.


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class AdminUserSerializer(ModelSerializer):

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data['password'])
            instance.save()

        return instance

    class Meta:
        model = User
        fields = "__all__"
