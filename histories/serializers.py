import json

from django.utils import timezone
from rest_framework import serializers

from bikes.serializers import BikeSerializer
from histories.models import UserHistory
from histories.utils import calculate_distance, calculate_duration


class LocationSerializer(serializers.Serializer):

    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


class RouteLineSerializer(serializers.ListSerializer):

    child = LocationSerializer()


class UserHistorySerializer(serializers.ModelSerializer):

    bike = BikeSerializer(read_only=True)

    class Meta:
        model = UserHistory
        fields = ("id", "bike", "selected_plan", "route_line")

    def to_representation(self, instance):
        user_history = super().to_representation(instance)
        user_history["bike"].pop("latitude")
        user_history["bike"].pop("longitude")
        user_history["timestamps"] = {}
        user_history["timestamps"]["borrow_date"] = str(instance.borrow_time.date().strftime("%B %d, %Y"))
        user_history["timestamps"]["borrow_time"] = str(timezone.localtime(instance.borrow_time).strftime("%I:%M %p"))
        if instance.return_time is None:
            duration = calculate_duration(instance.borrow_time, timezone.now())
        else:
            user_history["timestamps"]["return_date"] = str(instance.return_time.date().strftime("%B %d, %Y"))
            user_history["timestamps"]["return_time"] = str(timezone.localtime(instance.return_time).strftime("%I:%M %p"))
            duration = calculate_duration(instance.borrow_time, instance.return_time)
        distance = calculate_distance(instance.route_line)
        user_history["duration"] = duration
        user_history["distance"] = distance
        route_line = user_history.pop("route_line")
        user_history["route_line"] = json.loads(route_line)
        return user_history


class UserHistoryListSerializer(UserHistorySerializer):

    def to_representation(self, instance):
        user_history = super().to_representation(instance)
        user_history.pop("route_line")
        return user_history
