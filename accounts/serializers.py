from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers

from accounts.models import UserProfile, PointTransaction


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")


class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("gender", "phone_no", "user")

    def to_representation(self, instance):
        user_profile = super(UserProfileSerializer, self).to_representation(instance)
        user = user_profile.pop("user")
        for key in user:
            user_profile[key] = user[key]
        user = User.objects.get(username=user_profile.get("username"))
        user_profile["point"] = PointTransaction.get_point(user)
        return user_profile



