from django.contrib import admin
from django.contrib.admin import register
from django.utils import timezone

from accounts.models import UserProfile, ExtraUserProfile, UserHistory
from kmitl_bike_django.utils import AbstractAdmin


@register(UserProfile, site=admin.site)
class UserProfileAdmin(AbstractAdmin):

    class Meta:
        model = UserProfile


@register(ExtraUserProfile, site=admin.site)
class ExtraUserProfileAdmin(AbstractAdmin):

    class Meta:
        model = ExtraUserProfile


@register(UserHistory, site=admin.site)
class UserHistoryAdmin(AbstractAdmin):

    class Meta:
        model = UserHistory

    list_display = tuple(field.name for field in UserHistory._meta.get_fields()) + ('overdue',)

    exclude = ('created_date', 'updated_date', 'route_line')

    def overdue(self, instance):
        if not instance.return_time:
            return (instance.borrow_time - timezone.now()).min > instance.selected_plan.period
        return False
