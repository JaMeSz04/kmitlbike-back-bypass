from django.contrib import admin
from django.contrib.admin import register

from kmitl_bike_django.utils import AbstractAdmin
from reports.models import Feedback, Report


@register(Feedback, site=admin.site)
class FeedbackAdmin(AbstractAdmin):

    class Meta:
        model = Feedback


@register(Report, site=admin.site)
class ReportAdmin(AbstractAdmin):

    class Meta:
        model = Report
