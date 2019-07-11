from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.utils.crypto import get_random_string
from .models import VerificationToken
from user.models import User
from rest_framework.authtoken.models import Token


class MobileAuthViewSet(viewsets.ViewSet):
    permission_classes = ()
    @action(detail=False, methods=['post'])
    def login(self, request):

        # todo validate mobile number
        mobile = request.data["mobile"]
        print(mobile)
        code = get_random_string(length=6, allowed_chars='1234567890')
        print(code)
        # @todo send code to phone

        VerificationToken.objects.create(key=mobile, code=code)
        User.objects.get_or_create(mobile=mobile)

        return Response("Code created successfully")

    @action(detail=False, methods=['post'])
    def verify(self, request):
        mobile = request.data["mobile"]
        code = request.data["code"]

        # @todo
        try:
            VerificationToken.objects.get(key=mobile, code=code)
            user = User.objects.get(mobile=mobile)
        except (VerificationToken.DoesNotExist, User.DoesNotExist):
            return Response("verification error", status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        # todo return user permissions
        return Response({'token': token.key})
