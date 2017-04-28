from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import *

from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer
from kmitl_bike_django.utils import AbstractAPIView


class RegisterSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"] = serializers.CharField()
        self.fields["first_name"] = serializers.CharField(min_length=1, max_length=30)
        self.fields["last_name"] = serializers.CharField(min_length=1, max_length=30)
        self.fields["email"] = serializers.EmailField()
        self.fields["gender"] = serializers.IntegerField()
        self.fields["phone_no"] = serializers.CharField(min_length=10, max_length=12)

    def validate(self, attrs):
        try:
            gender = attrs.pop("gender")
            phone_no = attrs.pop("phone_no")
            user = User.objects.create(**attrs)
            user_profile, created = UserProfile.objects.get_or_create(user=user, gender=gender, phone_no=phone_no)
            serializer = UserProfileSerializer(user_profile)
            return serializer.data
        except IntegrityError:
            raise serializers.ValidationError("The user already exists.")
        except (TypeError, ValueError) as e:
            print(e)
            raise serializers.ValidationError("Enter a valid information.")

    def validate_gender(self, value):
        if value not in [gender[0] for gender in UserProfile.get_gender()]:
            raise serializers.ValidationError("Enter a valid gender.")
        return value


class RegisterView(AbstractAPIView, CreateModelMixin):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=HTTP_200_OK)
        error_message = self.get_error_message(serializer.errors)
        return Response({"message": error_message}, status=HTTP_400_BAD_REQUEST)
