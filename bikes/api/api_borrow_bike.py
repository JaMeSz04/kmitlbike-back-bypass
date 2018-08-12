
import json

from django.db import IntegrityError
from django.utils.decorators import method_decorator
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import *

from accounts.models import PointTransaction
from bikes.models import Bike, BikeUsagePlan
from bikes.utils import Sha256Hash
from histories.models import UserHistory
from histories.serializers import UserHistorySerializer, LocationSerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView



class BorrowBikeSerializer(serializers.Serializer):

    BORROW_COMMAND = "BORROW,<<MAC_ADDRESS>>,<<NONCE>>,<<PASSWORD>>"

    def __init__(self, *args, **kwargs):
        super(BorrowBikeSerializer, self).__init__(*args, **kwargs)
        self.fields["location"] = LocationSerializer()
        self.fields["nonce"] = serializers.IntegerField()
        self.fields["selected_plan"] = serializers.IntegerField()

    def validate(self, attrs):
        bike = self.context.get("bike")
        if not bike.is_available:
            raise serializers.ValidationError("The bike is already borrowed by another user.")
        bike.is_available = False

        nonce = attrs.get("nonce")
        bike_mac_address = bike.mac_address
        bike_key = bike.bike_key
        message = BorrowBikeSerializer.BORROW_COMMAND
        print(bike_mac_address)
        print(nonce)
        print(bike_key)
        message = message.replace("<<MAC_ADDRESS>>", bike_mac_address)\
            .replace("<<NONCE>>", str(nonce))\
            .replace("<<PASSWORD>>", bike_key)
        hashed_message = Sha256Hash.hash(message)
        user = self.context.get("request").user
        selected_plan = attrs.get("selected_plan")
        print(hashed_message)
        try:
            selected_plan = BikeUsagePlan.objects.get(id=selected_plan)
        except BikeUsagePlan.DoesNotExist:
            raise serializers.ValidationError("Bike usage plan does not exist.")
        try:
            if UserHistory.objects.filter(user=user, return_time=None).exists():
                raise serializers.ValidationError("You have not returned the previous bike yet.")
            if PointTransaction.get_point(user) - selected_plan.price >= 0:
                user_history = UserHistory.objects.create(user=user, bike=bike, selected_plan=selected_plan)
                location = attrs.get("location")
                route_line_history = json.loads(user_history.route_line)
                route_line_history += [location]
                user_history.route_line = json.dumps(route_line_history)
                user_history.save()
                PointTransaction.objects.create(user=user, point=-selected_plan.price,
                                                transaction_type=PointTransaction.Type.DEPOSIT)
                bike.save()
                user_history_serializer = UserHistorySerializer(user_history)
                return {"session": user_history_serializer.data,
                        "point": PointTransaction.get_point(user),
                        "message": hashed_message}
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
