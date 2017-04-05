from django.contrib.auth.models import User
from django.db import models

from bikes.models import Bike, BikeUsagePlan
from kmitl_bike_django.utils import AbstractModel


class UserProfile(AbstractModel):

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "Users\' Profiles"

    class Gender:
        MALE = 1
        FEMALE = 2
        OTHER = 3

    _gender = (
        (Gender.MALE, "Male"),
        (Gender.FEMALE, "Female"),
        (Gender.OTHER, "Other"),
    )

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    gender = models.IntegerField("Gender", null=False)
    phone_no = models.CharField("Phone no.", max_length=32, null=False)
    point = models.IntegerField("Point", null=False, default=100)

    def __str__(self):
        return self.user.username


class ExtraUserProfile(AbstractModel):

    class Meta:
        verbose_name = "Extra User Profile"
        verbose_name_plural = "Extra Users\' Profiles"

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    kmitl_id = models.CharField("KMITL ID", max_length=32, null=False, blank=True)
    first_name = models.CharField("First name", max_length=255, null=False, blank=True)
    last_name = models.CharField("Last name", max_length=255, null=False, blank=True)
    id_card = models.CharField("ID card", max_length=255, null=False, blank=True)
    phone_no = models.CharField("Phone no.", max_length=32, null=False, blank=True)
    faculty = models.CharField("Faculty", max_length=255, null=False, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    forward_email = models.EmailField("Forward email", null=True, blank=True)

    def __str__(self):
        return self.user.username


class UserHistory(AbstractModel):

    class Meta:
        verbose_name = "User History"
        verbose_name_plural = "Users\' Histories"

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, null=False, on_delete=models.CASCADE)
    selected_plan = models.ForeignKey(BikeUsagePlan, null=False, on_delete=models.CASCADE)
    borrow_time = models.DateTimeField("Borrow time", auto_now_add=True, null=False)
    return_time = models.DateTimeField("Return time", auto_now_add=False, auto_now=False, null=True)
    total_time = models.CharField("Total time", max_length=16, null=True)
    total_distance = models.CharField("Total distance", max_length=16, null=True)
    route_line = models.TextField("Route line", null=False, default="[]")

    def __str__(self):
        return self.user.username

