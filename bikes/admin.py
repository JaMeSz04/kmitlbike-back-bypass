from django.contrib import admin
from django.contrib.admin import register

from bikes.forms import BikeForm
from bikes.models import BikeModel, Bike, BikeUsagePlan
from kmitl_bike_django.utils import AbstractAdmin


@register(BikeModel, site=admin.site)
class BikeModelAdmin(AbstractAdmin):

    class Meta:
        model = BikeModel

    list_display = ("model_name", "image_thumbnail")

    def image_thumbnail(self, instance):
        return instance.get_thumbnail()

    image_thumbnail.short_description = 'Thumbnail'
    image_thumbnail.allow_tags = True


@register(Bike, site=admin.site)
class BikeAdmin(AbstractAdmin):

    class Meta:
        model = Bike

    list_display = ("bike_name", "bike_model", "is_available", "passcode")

    form = BikeForm


@register(BikeUsagePlan, site=admin.site)
class BikeUsagePlanAdmin(AbstractAdmin):

    class Meta:
        model = BikeUsagePlan

    list_display = ("plan_name", "period", "price")
