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


class Report(AbstractModel):

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    class Type:
        APP_PROBLEM = 1
        BIKE_PROBLEM = 2
        SUGGESTION = 3
        OTHER = 4

    _type = (
        (Type.APP_PROBLEM, "ปัญหาการใช้งานแอพ"),
        (Type.BIKE_PROBLEM, "ปัญหาการใช้งานจักรยาน"),
        (Type.SUGGESTION, "ข้อเสนอแนะ"),
        (Type.OTHER, "อื่น ๆ"),
    )

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    report_type = models.IntegerField("Report type", null=False, blank=False)
    detail = models.TextField("Report detail", null=False, blank=True)
