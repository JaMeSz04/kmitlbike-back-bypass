import json

from django.utils import timezone
from rest_framework import serializers

from bikes.models import Bike, BikeUsagePlan, BikeModel, BikeStatus
from accounts.serializers import UserProfileSerializer
from accounts.models import UserProfile
from histories.models import UserHistory
from histories.utils import calculate_distance,calculate_duration


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ("id", "bike_name", "bike_model", "barcode", "mac_address", "latitude", "longitude")

    def to_representation(self, instance):
        bike = super(BikeSerializer, self).to_representation(instance)
        bike_model = bike.pop("bike_model")
        bike_model_name = BikeModel.objects.get(id=bike_model).model_name
        bike["bike_model"] = bike_model_name
        return bike


class BikeUsagePlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = BikeUsagePlan
        fields = ("id", "plan_name", "price", "period")


class CurrentUsedBikeSerializer(serializers.ModelSerializer):
    bike = BikeSerializer(read_only=True)

    class Meta:
        model = UserHistory
        fields = ("id", "user", "bike", "selected_plan", "route_line")

    def to_representation(self, instance):
        user_history = super(CurrentUsedBikeSerializer, self).to_representation(instance)

        user_id = user_history.pop("user")
        user = UserProfile.objects.get(user_id=user_id)
        user_serializer = UserProfileSerializer(user)
        user_history["user"] = user_serializer.data

        user_history["bike"].pop("latitude")
        user_history["bike"].pop("longitude")

        selected_plan_id = user_history.pop("selected_plan")
        selected_plan = BikeUsagePlan.objects.get(id=selected_plan_id)
        plan_serializer = BikeUsagePlanSerializer(selected_plan)
        user_history["selected_plan"] = plan_serializer.data

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
        #user_history["route_line"] = json.loads(route_line)
        route = json.loads(route_line)
        user_history["route_line"] = route[len(route)-1]
        return user_history


class BikeStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = BikeStatus
        fields = ("id", "bike", "status")


