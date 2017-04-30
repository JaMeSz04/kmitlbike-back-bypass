from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers

from accounts.models import UserProfile, PointTransaction


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("gender", "phone_no", "user")

    def to_representation(self, instance):
        user_profile = super().to_representation(instance)
        user = user_profile.pop("user")
        for key in user:
            user_profile[key] = user[key]
        user_profile["point"] = PointTransaction.objects.filter(user__username=user_profile.get("username")).aggregate(Sum("point"))
        return user_profile



