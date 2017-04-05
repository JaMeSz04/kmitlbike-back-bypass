from django.contrib import admin
from django.contrib.admin import register

from bikes.forms import BikeForm
from bikes.models import BikeModel, Bike, BikeUsagePlan
from kmitl_bike_django.utils import AbstractAdmin


@register(BikeModel, site=admin.site)
class BikeModelAdmin(AbstractAdmin):

    class Meta:
        model = BikeModel


@register(Bike, site=admin.site)
class BikeAdmin(AbstractAdmin):

    class Meta:
        model = Bike

    form = BikeForm


@register(BikeUsagePlan, site=admin.site)
class BikeUsagePlanAdmin(AbstractAdmin):

    class Meta:
        model = BikeUsagePlan
