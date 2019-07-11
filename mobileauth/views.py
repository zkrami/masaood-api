from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.utils.crypto import get_random_string
from .models import VerificationToken
from user.models import User
from rest_framework.authtoken.models import Token


class MobileAuthViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def login(self, request):

        # todo validate mobile number
        mobile = request.data["mobile"]
        code = get_random_string(length=6, allowed_chars='1234567890')
        # @todo send code to phone

        VerificationToken.objects.create(key=mobile, code=code)
        User.get_or_create(mobile=mobile)

        return Response("Code created successfully")

    @action(detail=False, methods=['post'])
    def verify(self, request):
        mobile = request.data["mobile"]
        code = request.data["code"]

        VerificationToken.objects.get(key=mobile, code=code)

        user = User.objects.get(mobile=mobile)

        token = Token.objects.create(user=user)
        
        # todo return user permissions 
        return Response({'token': token.key})
