from django.contrib.auth.models import User
from django.utils import timezone
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


class PointTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PointTransaction
        fields = ("id", "point", "transaction_type", "comment")

    def to_representation(self, instance):
        point_transaction = super(PointTransactionSerializer, self).to_representation(instance)
        point_transaction["timestamps"] = {}
        point_transaction["timestamps"]["date"] = str(instance.created_date.date().strftime("%B %d, %Y"))
        point_transaction["timestamps"]["time"] = str(timezone.localtime(instance.created_date).strftime("%I:%M %p"))
        transaction_type = point_transaction.pop("transaction_type")
        for type_id, type_name in PointTransaction.get_type():
            if transaction_type == type_id:
                point_transaction["transaction_type"] = type_name
                return point_transaction
        point_transaction["transaction_type"] = transaction_type
        return point_transaction
