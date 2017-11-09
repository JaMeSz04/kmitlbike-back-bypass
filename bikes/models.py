from django.db import models
from location_field.models.plain import PlainLocationField

from bikes.utils import thumbnail_file_name
from kmitl_bike_django.settings import GOOGLE_DEFAULT_LOCATION
from kmitl_bike_django.utils import AbstractModel


class BikeModel(AbstractModel):

    class Meta:
        verbose_name = "Bike Model"
        verbose_name_plural = "Bike Models"

    model_name = models.CharField("Model name", max_length=255, unique=True, null=False, blank=False)
    bike_image = models.ImageField("Bike image", null=False, blank=True, upload_to=thumbnail_file_name)

    def __str__(self):
        return self.model_name

    def get_thumbnail(self):
        if self.bike_image:
            return u'<img src="%s" width=257 height=180 />' % self.bike_image.url
        return None


class Bike(AbstractModel):

    class Meta:
        verbose_name = "Bike"
        verbose_name_plural = "Bikes"

    bike_name = models.CharField("Bike name", max_length=64, unique=True, null=False, blank=False)
    bike_model = models.ForeignKey(BikeModel, null=False, blank=False)
    mac_address = models.CharField("MAC address", max_length=32, unique=True, null=True, blank=True)
    barcode = models.CharField("Barcode", unique=True, max_length=255, null=False, blank=False)
    bike_key = models.CharField("Bike key", max_length=128, unique=True, null=False, blank=False)
    serial_no = models.CharField("Serial no.", unique=True, max_length=32, null=True, blank=True)
    is_available = models.BooleanField("Is available", default=True, null=False, blank=False)
    location = PlainLocationField(zoom=15, null=False, blank=False, default=GOOGLE_DEFAULT_LOCATION)

    def __str__(self):
        return self.bike_name

    @property
    def latitude(self):
        return float(self.location.split(",")[0])

    @property
    def longitude(self):
        return float(self.location.split(",")[1])

    @staticmethod
    def autocomplete_search_fields():
        return "bike_name", "mac_address"


class BikePassword(AbstractModel):

    class Meta:
        verbose_name = "Bike Password"
        verbose_name_plural = "Bike Passwords"

    bike = models.OneToOneField(Bike, null=False, blank=False)

    def __str__(self):
        return self.bike.bike_name


class BikeUsagePlan(AbstractModel):

    class Meta:
        verbose_name = "Bike Usage Plan"
        verbose_name_plural = "Bike Usage Plans"

    plan_name = models.CharField("Plan name", max_length=255, null=False, blank=False)
    period = models.IntegerField("Period (seconds)", null=False, blank=False)
    price = models.IntegerField("Price", null=False, blank=False)

    def __str__(self):
        return self.plan_name
