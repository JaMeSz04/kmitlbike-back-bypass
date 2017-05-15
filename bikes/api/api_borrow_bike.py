from django.db import IntegrityError
from django.utils.decorators import method_decorator
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import *

from accounts.models import PointTransaction
from bikes.models import BikeUsagePlan, Bike
from bikes.serializers import BikeSerializer
from bikes.utils import RSAEncryption, is_mac_address
from histories.models import UserHistory
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class BorrowBikeSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["command"] = serializers.CharField()
        self.fields["selected_plan"] = serializers.IntegerField()

    def validate(self, attrs):

        command = attrs.get("command")[1:-1].split(",")

        if len(command) != 3:
            raise serializers.ValidationError("Invalid command.")
        if command[0] != "BORROW":
            raise serializers.ValidationError("Incorrect command.")
        if not is_mac_address(command[1]):
            raise serializers.ValidationError("Invalid MAC address.")

        encryption_suite = RSAEncryption()
        message = encryption_suite.encrypt(command)
        mac_address = command[1]
        try:
            bike = Bike.objects.get(mac_address=mac_address)
        except Bike.DoesNotExist:
            raise serializers.ValidationError("Bike does not exist.")
        if not bike.is_available:
            raise serializers.ValidationError("The bike is already borrowed by another user.")
        bike.is_available = False

        user = self.context.get("request").user
        selected_plan = attrs.get("selected_plan")
        try:
            selected_plan = BikeUsagePlan.objects.get(id=selected_plan)
        except BikeUsagePlan.DoesNotExist:
            raise serializers.ValidationError("Bike usage plan does not exist.")
        try:
            if UserHistory.objects.filter(user=user, return_time=None).exists():
                raise serializers.ValidationError("You have not returned the previous bike yet.")
            if PointTransaction.get_point(user) - selected_plan.price >= 0:
                UserHistory.objects.create(user=user, bike=bike, selected_plan=selected_plan)
                PointTransaction.objects.create(user=user, point=-selected_plan.price,
                                                transaction_type=PointTransaction.Type.DEPOSIT)
                bike.save()
                bike_serializer = BikeSerializer(bike)
                return {"bike": bike_serializer.data,
                        "message": message}
            else:
                raise serializers.ValidationError("Insufficient points to borrow.")
        except IntegrityError:
            raise serializers.ValidationError("Invalid parameters.")


class BorrowBikeView(AbstractAPIView):

    serializer_class = BorrowBikeSerializer

    @method_decorator(token_required)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=HTTP_200_OK)
        error_message = self.get_error_message(serializer.errors)
        return Response({"detail": error_message}, status=HTTP_400_BAD_REQUEST)


def as_view():
    return BorrowBikeView.as_view()
