from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("gender", "phone_no", "point", "user")
        read_only_fields = ("point",)

    def to_representation(self, instance):
        user_profile = super().to_representation(instance)
        user = user_profile.pop("user")
        for key in user:
            user_profile[key] = user[key]
        return user_profile



