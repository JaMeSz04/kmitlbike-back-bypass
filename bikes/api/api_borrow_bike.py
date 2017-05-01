from django.db import IntegrityError
from django.utils.decorators import method_decorator
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import *

from accounts.models import PointTransaction
from bikes.models import Bike, BikeUsagePlan
from bikes.serializers import BikeSerializer
from histories.models import UserHistory
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class BorrowBikeSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["selected_plan"] = serializers.IntegerField()

    def validate(self, attrs):
        bike = self.context.get("bike")
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
                return bike_serializer.data
            else:
                raise serializers.ValidationError("Insufficient points to borrow.")
        except IntegrityError:
            raise serializers.ValidationError("Invalid parameters.")


class BorrowBikeView(AbstractAPIView):

    serializer_class = BorrowBikeSerializer

    def get_object(self, bike_id):
        try:
            return Bike.objects.get(id=bike_id)
        except Bike.DoesNotExist:
            raise NotFound("Bike does not exist.")

    def get_serializer_context(self):
        return {
            "request": self.request,
            "format": self.format_kwarg,
            "view": self,
            "bike": self.get_object(self.kwargs["bike_id"])}

    @method_decorator(token_required)
    def post(self, request, bike_id=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=HTTP_200_OK)
        error_message = self.get_error_message(serializer.errors)
        return Response({"detail": error_message}, status=HTTP_400_BAD_REQUEST)


def as_view():
    return BorrowBikeView.as_view()
