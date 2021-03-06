from django.db import IntegrityError
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import *

from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer
from kmitl_bike_django.utils import AbstractAPIView


class AccessTokenSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super(AccessTokenSerializer, self).__init__(*args, **kwargs)
        self.fields["token"] = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get("token")
        try:
            token, created = Token.objects.get_or_create(key=token)
            user = token.user
            user.last_login = timezone.now()
            user.save()

            user_profile = UserProfile.objects.get(user=user)
            user.last_login = timezone.now()
            user.save()
            serializer = UserProfileSerializer(user_profile)
            data = serializer.data
            data["token"] = str(token)

            return data
        except IntegrityError:
            raise serializers.ValidationError("The token is already expired.")


class AccessTokenView(AbstractAPIView):

    serializer_class = AccessTokenSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=HTTP_200_OK)
        error_message = self.get_error_message(serializer.errors)
        return Response({"detail": error_message}, status=HTTP_400_BAD_REQUEST)


def as_view():
    return AccessTokenView.as_view()
