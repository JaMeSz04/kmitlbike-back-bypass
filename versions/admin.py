from django.contrib import admin
from django.contrib.admin import register

from kmitl_bike_django.utils import AbstractAdmin
from versions.models import AppVersion, AndroidAppVersion, IosAppVersion


class AppVersionAdmin(AbstractAdmin):

    class Meta:
        model = AppVersion

    list_display = ("version_code", "version_name", "platform")


@register(AndroidAppVersion, site=admin.site)
class AndroidAppVersionAdmin(AppVersionAdmin):

    class Meta:
        model = AndroidAppVersion


@register(IosAppVersion, site=admin.site)
class IosAppVersionAdmin(AppVersionAdmin):

    class Meta:
        model = IosAppVersion
