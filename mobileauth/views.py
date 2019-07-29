from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.utils.crypto import get_random_string
from .models import VerificationToken
from user.models import User
from rest_framework.authtoken.models import Token
from user.serializers import UserDetailsSerializer
from django.contrib.auth.models import Group

class MobileAuthViewSet(viewsets.ViewSet):
    permission_classes = ()
    @action(detail=False, methods=['post'])
    def login(self, request):

        # todo validate mobile number
        mobile = request.data["mobile"]
        code = get_random_string(length=6, allowed_chars='1234567890')
        code = '666666'
        # @todo send code to phone

        token, tokenCreated = VerificationToken.objects.get_or_create(
            key=mobile, code=code)
        # update expiration

        user, created = User.objects.get_or_create(mobile=mobile)
        # add user role 
        group = Group.objects.get(name='user')
        user.groups.add(group)

        return Response({"message": "Created successfully", "verified": user.verified})

    @action(detail=False, methods=['post'])
    def verify(self, request):
        mobile = request.data["mobile"]
        code = request.data["code"]

        # @todo code expiration
        try:
            VerificationToken.objects.get(key=mobile, code=code)
            user = User.objects.get(mobile=mobile)
        except (VerificationToken.DoesNotExist, User.DoesNotExist):
            return Response("verification error", status=status.HTTP_400_BAD_REQUEST)

        user.verified = True
        user.save()

        userData = UserDetailsSerializer(user).data    

        token, _ = Token.objects.get_or_create(user=user)
        # todo return user permissions
        return Response({'token': token.key, 'user': userData})
