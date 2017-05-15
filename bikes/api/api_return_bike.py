import json

from django.utils import timezone
from django.utils.decorators import method_decorator
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import *

from accounts.models import PointTransaction
from bikes.models import Bike
from histories.models import UserHistory
from histories.serializers import RouteLineSerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class ReturnBikeSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["latitude"] = serializers.FloatField()
        self.fields["longitude"] = serializers.FloatField()
        self.fields["route_line"] = RouteLineSerializer()

    def validate(self, attrs):
        user = self.context.get("request").user
        user_history = UserHistory.objects.filter(user=user, return_time__isnull=True).last()
        if user_history is None:
            raise serializers.ValidationError("You already returned the bike.")
        route_line = attrs.get("route_line")
        route_line_history = json.loads(user_history.route_line)
        route_line_history += route_line
        user_history.route_line = json.dumps(route_line_history)
        user_history.return_time = timezone.now()
        user_history.save()

        latitude = attrs.get("latitude")
        longitude = attrs.get("longitude")

        user_history.bike.location = "%s,%s" % (latitude, longitude)
        user_history.bike.is_available = True
        user_history.bike.save()

        total_duration = (user_history.return_time - user_history.borrow_time).total_seconds()
        if total_duration <= user_history.selected_plan.period:
            PointTransaction.objects.create(user=user, point=user_history.selected_plan.price,
                                            transaction_type=PointTransaction.Type.REFUND)
        else:
            minutes_overdue = total_duration - user_history.selected_plan // 60
            PointTransaction.objects.create(user=user, point=-minutes_overdue,
                                            transaction_type=PointTransaction.Type.PENALTY)
        point_left = PointTransaction.get_point(user)
        return {"point": point_left}


class ReturnBikeView(AbstractAPIView):

    serializer_class = ReturnBikeSerializer

    @method_decorator(token_required)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=HTTP_200_OK)
        error_message = self.get_error_message(serializer.errors)
        return Response({"detail": error_message}, status=HTTP_400_BAD_REQUEST)


def as_view():
    return ReturnBikeView.as_view()
