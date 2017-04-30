from django.contrib import admin
from django.contrib.admin import register

from accounts.models import UserProfile, PointTransaction
from kmitl_bike_django.utils import AbstractAdmin


@register(UserProfile, site=admin.site)
class UserProfileAdmin(AbstractAdmin):

    class Meta:
        model = UserProfile

    list_display = ("user", "gender", "phone_no", "point")

    def point(self, instance):
        return PointTransaction.get_point(instance.user)


# @register(UserExtraProfile, site=admin.site)
# class UserExtraProfileAdmin(AbstractAdmin):
#
#     class Meta:
#         model = UserExtraProfile
#
#     list_display = ("user", "first_name", "last_name", "phone_no", "faculty")


@register(PointTransaction, site=admin.site)
class PointTransactionAdmin(AbstractAdmin):

    class Meta:
        model = PointTransaction

    list_display = ("user", "point", "transaction_type")
