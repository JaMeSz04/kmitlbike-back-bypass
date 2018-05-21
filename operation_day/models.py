from django.db import models

from kmitl_bike_django.utils import AbstractModel


class OperationDays(AbstractModel):
    class Meta:
        verbose_name = "Operation Day"
        verbose_name_plural = "Operation Days"

    day = models.CharField("Day", max_length=64, unique=True, null=False)
    open_time = models.TimeField("Open Time", null=False)
    close_time = models.TimeField("Close Time", null=False)
    is_operated = models.BooleanField("Is Operated", null=False, default=1)

    def __str__(self):
        return self.day


class Holidays(AbstractModel):
    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"

    day = models.CharField("Day", max_length=64, null=False)
    date = models.DateField("date", null=False)

    def __str__(self):
        return self.day
