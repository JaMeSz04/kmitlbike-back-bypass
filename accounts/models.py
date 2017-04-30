from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

from bikes.models import Bike, BikeUsagePlan
from kmitl_bike_django.utils import AbstractModel


class UserProfile(AbstractModel):

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "Users\' Profiles"

    class Gender(object):
        MALE = 1
        FEMALE = 2
        OTHER = 3

    _gender = (
        (Gender.MALE, "Male"),
        (Gender.FEMALE, "Female"),
        (Gender.OTHER, "Other"),
    )

    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    gender = models.IntegerField("Gender", null=False, blank=False, choices=_gender)
    phone_no = models.CharField("Phone no.", max_length=32, null=False, blank=False)

    def __str__(self):
        return self.user.username

    @staticmethod
    def get_gender():
        return UserProfile._gender


class UserExtraProfile(AbstractModel):

    class Meta:
        verbose_name = "User Extra Profile"
        verbose_name_plural = "Users\' Extra Profiles"

    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
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


class PointTransaction(AbstractModel):

    class Meta:
        verbose_name = "Point Transaction"
        verbose_name_plural = "Point Transactions"

    class Type(object):
        INITIAL = 1
        DEPOSIT = 2
        REFUND = 3
        PENALTY = 4
        SPECIAL = 5

    _type = (
        (Type.INITIAL, "Initial"),
        (Type.DEPOSIT, "Deposit"),
        (Type.REFUND, "Refund"),
        (Type.PENALTY, "Penalty"),
        (Type.SPECIAL, "Special")
    )

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    point = models.IntegerField("Point", null=False, blank=False)
    transaction_type = models.IntegerField("Transaction type", null=False, blank=False, choices=_type)

    @staticmethod
    def get_point(user):
        return PointTransaction.objects.filter(user=user).aggregate(Sum("point"))["point__sum"]

    def __str__(self):
        return str(self.id)
