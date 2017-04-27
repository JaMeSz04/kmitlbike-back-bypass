from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    user_profile = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


# class UserProfileSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = UserProfile
#         fields = ('gender', 'phone_no', 'point')
