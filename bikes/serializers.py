from rest_framework import serializers

from bikes.models import Bike, BikeUsagePlan, BikeModel


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
