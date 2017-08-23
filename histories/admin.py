from django.contrib import admin
from django.contrib.admin import register
from django.utils import timezone

from histories.models import UserHistory
from kmitl_bike_django.utils import AbstractAdmin


@register(UserHistory, site=admin.site)
class UserHistoryAdmin(AbstractAdmin):

    class Meta:
        model = UserHistory

    list_display = ("user", "bike", "selected_plan", "borrow_time", "return_time", "overdue")

    def overdue(self, instance):
        if not instance.return_time:
            return (timezone.now() - instance.borrow_time).total_seconds() > instance.selected_plan.period
        return (instance.return_time - instance.borrow_time).total_seconds() > instance.selected_plan.period
