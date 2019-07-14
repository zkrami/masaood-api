from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
import rest_framework.status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import ParseError
from .models import User
from .serializers import UserSerializer, AdminUserSerializer
from rest_framework.decorators import action

from rest_framework.generics import RetrieveUpdateAPIView


class UserViewSet(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


    def get_object(self):
        return self.request.user


class AdminUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = AdminUserSerializer
