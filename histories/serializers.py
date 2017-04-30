from rest_framework import serializers


class LocationSerializer(serializers.Serializer):

    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


class RouteLineSerializer(serializers.ListSerializer):

    child = LocationSerializer()
