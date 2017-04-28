from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import *

from accounts.backends import KMITLBackend
from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer
from kmitl_bike_django.utils import AbstractAPIView


class LoginSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"] = serializers.CharField()
        self.fields["password"] = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        result, token = KMITLBackend.authenticate(username, password)
        if result == KMITLBackend.Status.ALREADY_EXISTS:
            if token:
                user = token.user
                if user.is_active:
                    user_profile = UserProfile.objects.get(user=user)
                    serializer = UserProfileSerializer(user_profile)
                    data = serializer.data
                    data["result"] = result
                    return data
                else:
                    raise serializers.ValidationError("This account has been suspended. Please contact our staff for more detail.")
        elif result == KMITLBackend.Status.FIRST_TIME:
            return {"result": result,
                    "username": username}
        else:
            raise serializers.ValidationError("The username or password is incorrect.")


class LoginView(AbstractAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=HTTP_200_OK)
        error_message = self.get_error_message(serializer.errors)
        return Response({"message": error_message}, status=HTTP_400_BAD_REQUEST)

