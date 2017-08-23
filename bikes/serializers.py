from rest_framework import serializers

from bikes.models import Bike, BikeUsagePlan


class BikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bike
        fields = ("id", "bike_name", "bike_model", "barcode", "mac_address", "latitude", "longitude")


class BikeUsagePlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = BikeUsagePlan
        fields = ("id", "plan_name", "price")
