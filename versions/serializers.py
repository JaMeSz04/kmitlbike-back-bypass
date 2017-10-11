from rest_framework import serializers

from versions.models import AppVersion


class AppVersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppVersion
        fields = ("platform", "version_code", "url")
