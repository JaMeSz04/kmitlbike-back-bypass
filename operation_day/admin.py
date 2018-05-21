from django.contrib import admin
from django.contrib.admin import register

from operation_day.models import OperationDays, Holidays
from kmitl_bike_django.utils import AbstractAdmin


@register(OperationDays, site=admin.site)
class OperationDaysAdmin(AbstractAdmin):

    class Meta:
        model = OperationDays

    list_display = ("day", "open_time", "close_time", "is_operated")


@register(Holidays, site=admin.site)
class HolidaysAdmin(AbstractAdmin):

    class Meta:
        model = Holidays

    list_display = ("day", "date")
