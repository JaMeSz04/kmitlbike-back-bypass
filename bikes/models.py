from django.db import models

from kmitl_bike_django.utils import AbstractModel


class BikeModel(AbstractModel):

    class Meta:
        verbose_name = "Bike Model"
        verbose_name_plural = "Bike Models"

    model_name = models.CharField("Model name", max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.model_name


class Bike(AbstractModel):

    class Meta:
        verbose_name = "Bike"
        verbose_name_plural = "Bikes"

    bike_name = models.CharField("Bike name", max_length=64, unique=True, null=False, blank=False)
    bike_model = models.ForeignKey(BikeModel, null=False, blank=False)
    mac_addr = models.CharField("MAC address", max_length=32, unique=True, null=True, blank=True)
    serial_no = models.CharField("Serial no.", unique=True, max_length=32, null=True)
    barcode = models.CharField("Barcode", unique=True, max_length=16, null=True)
    is_available = models.BooleanField("Is available", default=True, null=False)
    current_lat = models.CharField("Current latitude", max_length=64, null=False)
    current_long = models.CharField("Current longitude", max_length=64, null=False)
    passcode = models.CharField("Passcode", max_length=32, null=False)

    def __str__(self):
        return self.bike_name


class BikeUsagePlan(AbstractModel):

    class Meta:
        verbose_name = "Bike Usage Plan"
        verbose_name_plural = "Bike Usage Plans"

    plan_name = models.CharField("Plan name", max_length=255, null=False, blank=False)
    period = models.IntegerField("Period (minutes)", null=False, blank=False)
    price = models.IntegerField("Price", null=False, blank=False)

    def __str__(self):
        return self.plan_name
