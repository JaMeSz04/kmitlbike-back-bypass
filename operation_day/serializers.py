from rest_framework import serializers

from operation_day.models import OperationDays, Holidays


class OperationDaysSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OperationDays
        fields = ("day", "open_time", "close_time", "is_operate")


class HolidaysSerializers(serializers.ModelSerializer):
    class Meta:
        model = Holidays
        fields = ("day", "date")