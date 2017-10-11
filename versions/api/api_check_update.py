from packaging.version import Version, InvalidVersion
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import *

from kmitl_bike_django.utils import AbstractAPIView
from versions.models import AppVersion
from versions.serializers import AppVersionSerializer


class CheckUpdateSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super(CheckUpdateSerializer, self).__init__(*args, **kwargs)
        self.fields["platform"] = serializers.CharField()
        self.fields["version_code"] = serializers.CharField()

    def validate(self, attrs):
        platform = attrs.get("platform")
        version_code = attrs.get("version_code")
        app_version = AppVersion.objects.filter(platform=platform).last()
        if app_version is None:
            raise serializers.ValidationError("No version available.")
        try:
            current_version = Version(version_code)
            latest_version = Version(app_version.version_code)
            if current_version < latest_version:
                data = AppVersionSerializer(app_version).data
                print(data)
                data["required_update"] = True
                return data
            return {"required_update": False}
        except InvalidVersion:
            raise serializers.ValidationError("Invalid app version.")


class CheckUpdateView(AbstractAPIView):

    serializer_class = CheckUpdateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=HTTP_200_OK)
        error_message = self.get_error_message(serializer.errors)
        return Response({"detail": error_message}, status=HTTP_400_BAD_REQUEST)


def as_view():
    return CheckUpdateView.as_view()
