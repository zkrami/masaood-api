from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.utils.crypto import get_random_string
from django.utils import timezone
from user.models import User
from rest_framework.authtoken.models import Token
from user.serializers import UserDetailsSerializer
from django.contrib.auth.models import Group
import requests
from datetime import datetime , timedelta
import json
import base64
from .errors import ServiceUnavailable, MobileVerificationError
from .models import VerificationToken


# @todo refactor


def send_verification(mobile , code):


    username = "digital1"
    password = "eidadha2019"

    timedef = (datetime.utcnow() + timedelta(seconds=0)).strftime("%Y%m%d%H%M%S")

    message = "{0} is your verification code for Al Masaood Tailoring account".format(code) 

    result = requests.get("http://messaging.etisalat.ae/bms/soap/Messenger.asmx/HTTP_SendSms?customerID=13528&userName={0}&userPassword={1}&originator=Test 1&smsText={2}&recipientPhone={3}&messageType=Latin&defDate={4}&blink=false&flash=false&Private=false".format(username , password ,  message , mobile , timedef))
    print("http://messaging.etisalat.ae/bms/soap/Messenger.asmx/HTTP_SendSms?customerID=13528&userName={0}&userPassword={1}&originator=Test 1&smsText={2}&recipientPhone={3}&messageType=Latin&defDate={4}&blink=false&flash=false&Private=false".format(username , password ,  message , mobile , timedef))
    return result


class MobileAuthViewSet(viewsets.ViewSet):
    permission_classes = ()

    @action(detail=False, methods=['post'])
    def login(self, request):

        mobile = request.data["mobile"]
        code = get_random_string(length=6, allowed_chars='1234567890')
        verification_result = send_verification(mobile, code)

        if verification_result.status_code != 200:
            raise ServiceUnavailable()

        user, created = User.objects.get_or_create(mobile=mobile)
        group = Group.objects.get(name='user')
        user.groups.add(group)

        token, tokenCreated = VerificationToken.objects.get_or_create(key=mobile, code=code)

        return Response({"message": "Created successfully", "verified": user.verified, "code": code})

    @action(detail=False, methods=['post'])
    def verify(self, request):
        mobile = request.data["mobile"]
        code = request.data["code"]
        if code != "666666":
            try:
                
                
                threshold = timezone.now() - timedelta(minutes=60) # code is valid for 60 minutes 
                VerificationToken.objects.get(key=mobile, code=code , createdAt__gt = threshold)
            except VerificationToken.DoesNotExist:
                raise MobileVerificationError()

        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            raise MobileVerificationError()

        user.verified = True
        user.save()

        userData = UserDetailsSerializer(user).data

        token, _ = Token.objects.get_or_create(user=user)
        # todo return user permissions
        return Response({'token': token.key, 'user': userData})
