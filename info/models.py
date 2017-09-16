# coding=utf-8
from django.db import models

from kmitl_bike_django.utils import AbstractModel


class Position(AbstractModel):

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    name = models.CharField("Position name", max_length=128, null=False, blank=False)
    priority = models.PositiveIntegerField("Priority", null=False, blank=False)

    def __str__(self):
        return self.name


class Credit(AbstractModel):

    class Meta:
        verbose_name = "Credit"
        verbose_name_plural = "Credits"

    name = models.CharField("Name", max_length=64, null=False, blank=False)
    position = models.ForeignKey(Position, null=False, blank=False)

    def __str__(self):
        return self.name


class License(AbstractModel):

    class Meta:
        verbose_name = "License"
        verbose_name_plural = "Licenses"

    name = models.CharField("Name", max_length=128, null=False, blank=False)
    copyright = models.CharField("Copyright", max_length=128, null=False, blank=False)
    url = models.CharField("Project URL", max_length=128, null=False, blank=True)
    license = models.CharField("License", max_length=128, null=False, blank=True)

    def __str__(self):
        return self.name
