from django.contrib import admin
from django.contrib.admin import register
from django.utils import timezone

from accounts.models import UserHistory
from kmitl_bike_django.utils import AbstractAdmin


@register(UserHistory, site=admin.site)
class UserHistoryAdmin(AbstractAdmin):

    class Meta:
        model = UserHistory

    list_display = ('user', 'bike', 'selected_plan', 'borrow_time', 'return_time', 'overdue')

    def overdue(self, instance):
        if not instance.return_time:
            return (instance.borrow_time - timezone.now()).min > instance.selected_plan.period
        return False
