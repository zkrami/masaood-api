from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action 
# Create your views here.
from .serializers import PasswordTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response 

class PasswordAuthTokenView(ViewSet):
    throttle_classes = ()
    permission_classes = ()
    serializer_class = PasswordTokenSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})