# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

from kmitl_bike_django.utils import AbstractModel


class Feedback(AbstractModel):

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedback"

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    like = models.BooleanField("Like", null=False, blank=False)
    comment = models.TextField("Comment", null=False, blank=True)

    def __str__(self):
        return str(self.id)


class Report(AbstractModel):

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    class Type:
        AUTOMATIC = 0
        APP_PROBLEM = 1
        BIKE_PROBLEM = 2
        SUGGESTION = 3
        OTHER = 4

    _type = (
        (Type.AUTOMATIC, "Automatic"),
        (Type.APP_PROBLEM, "App Usage Problem"),
        (Type.BIKE_PROBLEM, "Bike Usage Problem"),
        (Type.SUGGESTION, "Suggestions"),
        (Type.OTHER, "Other"),
    )

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    report_type = models.IntegerField("Report type", null=False, blank=False)
    detail = models.TextField("Report detail", null=False, blank=False)

    @staticmethod
    def get_type():
        return Report._type[1:]

    def __str__(self):
        return str(self.id)
