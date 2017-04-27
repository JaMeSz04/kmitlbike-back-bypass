from django.contrib import admin
from django.contrib.admin import register

from info.models import Credit, Position
from kmitl_bike_django.utils import AbstractAdmin


@register(Position, site=admin.site)
class PositionAdmin(AbstractAdmin):

    class Meta:
        model = Position

    list_display = ('name', 'priority')


@register(Credit, site=admin.site)
class CreditAdmin(AbstractAdmin):

    class Meta:
        model = Credit

    list_display = ('name', 'position')
