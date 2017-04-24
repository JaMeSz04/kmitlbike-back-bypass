from django.contrib import admin
from django.contrib.admin import register

from bikes.forms import BikeForm
from bikes.models import BikeModel, Bike, BikeUsagePlan
from kmitl_bike_django.utils import AbstractAdmin


@register(BikeModel, site=admin.site)
class BikeModelAdmin(AbstractAdmin):

    class Meta:
        model = BikeModel

    list_display = ('model_name',)


@register(Bike, site=admin.site)
class BikeAdmin(AbstractAdmin):

    class Meta:
        model = Bike

    list_display = ('bike_name', 'bike_model', 'is_available', 'passcode')

    form = BikeForm


@register(BikeUsagePlan, site=admin.site)
class BikeUsagePlanAdmin(AbstractAdmin):

    class Meta:
        model = BikeUsagePlan

    list_display = ('plan_name', 'period', 'price')
