from django.contrib import admin
from django.contrib.admin import register

from kmitl_bike_django.utils import AbstractAdmin
from services.models import AppVersion, AndroidAppVersion, IosAppVersion


@register(AppVersion, site=admin.site)
class AppVersionAdmin(AbstractAdmin):

    class Meta:
        model = AppVersion


@register(AndroidAppVersion, site=admin.site)
class AndroidAppVersionAdmin(AbstractAdmin):

    class Meta:
        model = AndroidAppVersion


@register(IosAppVersion, site=admin.site)
class IosAppVersionAdmin(AbstractAdmin):

    class Meta:
        model = IosAppVersion
