from django.contrib.auth.models import AnonymousUser
from django.utils.decorators import method_decorator
from rest_framework import serializers
from rest_framework.exceptions import NotFound, AuthenticationFailed
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.status import *

from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class ProfileSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"] = serializers.EmailField(required=False)
        self.fields["gender"] = serializers.IntegerField(required=False)
        self.fields["phone_no"] = serializers.CharField(required=False, min_length=10, max_length=12)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr in self.fields:
                if attr == "email":
                    setattr(instance.user, attr, value)
                else:
                    setattr(instance, attr, value)
            else:
                raise serializers.ValidationError("Invalid parameters.")
        instance.save()
        return instance


class ProfileView(AbstractAPIView, RetrieveModelMixin, UpdateModelMixin):

    serializer_class = ProfileSerializer

    def get_object(self, request):
        if type(request.user) is not AnonymousUser:
            user_profile = UserProfile.objects.get(user=request.user)
            return user_profile
        else:
            raise NotFound("User does not exist.")

    @method_decorator(token_required)
    def get(self, request, user_id):
        if int(user_id) is request.user.id:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                instance = self.get_object(request)
                user_profile_serializer = UserProfileSerializer(instance)
                return Response(user_profile_serializer.data, status=HTTP_200_OK)
            error_message = self.get_error_message(serializer.errors)
            return Response({"detail": error_message}, status=HTTP_400_BAD_REQUEST)
        raise AuthenticationFailed()

    @method_decorator(token_required)
    def post(self, request, user_id):
        if int(user_id) is request.user.id:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                instance = self.get_object(request)
                serializer.update(instance, request.data)
                user_profile_serializer = UserProfileSerializer(instance)
                return Response(user_profile_serializer.data, status=HTTP_200_OK)
            error_message = self.get_error_message(serializer.errors)
            return Response({"detail": error_message}, status=HTTP_400_BAD_REQUEST)
        raise AuthenticationFailed()
