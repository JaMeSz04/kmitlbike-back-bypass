from django.contrib import admin
from django.contrib.admin import register

from info.models import Credit, Position, License
from kmitl_bike_django.utils import AbstractAdmin


@register(Position, site=admin.site)
class PositionAdmin(AbstractAdmin):

    class Meta:
        model = Position

    list_display = ("name", "priority")


@register(Credit, site=admin.site)
class CreditAdmin(AbstractAdmin):

    class Meta:
        model = Credit

    list_display = ("name", "position")


@register(License, site=admin.site)
class LicenseAdmin(AbstractAdmin):

    class Meta:
        model = License

    list_display = ("name", "copyright", "url")
