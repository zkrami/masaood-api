from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
import rest_framework.status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import ParseError
from .models import User
from .serializers import UserSerializer, AdminUserSerializer, GroupSerializer, AdminDetailUserSerializer , UserDetailsSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from shared.mixins.per_action_serializer import PerActionSerializerMixin

from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth.models import Group


class UserViewSet(PerActionSerializerMixin,  RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer_action_classes = {
        'GET': UserDetailsSerializer , 
    }
    permission_classes = (IsAuthenticated,)
    filterset_fields = []

    def get_object(self):
        return self.request.user


class AdminUserViewSet(PerActionSerializerMixin, ModelViewSet):
    queryset = User.objects.all()
    permission_classes = ()
    serializer_class = AdminUserSerializer
    serializer_action_classes = {
        'list': AdminDetailUserSerializer,
        'retrieve': AdminDetailUserSerializer
    }
    filterset_fields = []


class GroupsViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Group.objects.all()
    permission_classes = ()
    serializer_class = GroupSerializer
