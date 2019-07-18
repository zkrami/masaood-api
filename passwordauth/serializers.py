from django.contrib.auth import authenticate
from rest_framework import serializers
from passwordauth.backend import EmailModelBackend


class PasswordTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # todo refactor 
            user = EmailModelBackend().authenticate(request=self.context.get('request'),
                                                  username=email, password=password)
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
