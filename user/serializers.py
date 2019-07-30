from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, RelatedField, CharField
from .models import User
from center.models import Center
# Create your models here.
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password


class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ("first_name", "last_name", "email", "status", "groups" , "center")


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # editable fields by user
        fields = ("first_name", "last_name", "email")


class AdminUserSerializer(ModelSerializer):

    groupsId = PrimaryKeyRelatedField(
        allow_empty=False, many=True, queryset=Group.objects.all(), source="groups")
    centerId = PrimaryKeyRelatedField(
        required=False, queryset=Center.objects.all(), source="center")

    def validate_password(self, value):
        return make_password(value)

    class Meta:
        model = User
        exclude = ("groups", "center",)


class AdminDetailUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depth = 1


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
