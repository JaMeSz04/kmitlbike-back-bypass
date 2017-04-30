from django.contrib.auth.models import User
from django.db import models

from bikes.models import Bike, BikeUsagePlan
from kmitl_bike_django.utils import AbstractModel


class UserHistory(AbstractModel):

    class Meta:
        verbose_name = "User\'s History"
        verbose_name_plural = "User\'s Histories"

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, null=False, on_delete=models.CASCADE)
    selected_plan = models.ForeignKey(BikeUsagePlan, null=False, on_delete=models.CASCADE)
    borrow_time = models.DateTimeField("Borrow time", auto_now_add=True, null=False, blank=False)
    return_time = models.DateTimeField("Return time", auto_now_add=False, auto_now=False, null=True, blank=True)
    route_line = models.TextField("Route line", null=False, blank=False, default="[]")

    def __str__(self):
        return self.user.username

