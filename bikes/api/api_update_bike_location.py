import json

from django.utils import timezone
from django.utils.decorators import method_decorator
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import *

from bikes.models import Bike
from histories.models import UserHistory
from histories.serializers import RouteLineSerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class UpdateBikeLocationSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["latitude"] = serializers.FloatField()
        self.fields["longitude"] = serializers.FloatField()
        self.fields["route_line"] = RouteLineSerializer()

    def validate(self, attrs):
        bike = self.context.get("bike")
        user = self.context.get("request").user
        user_history = UserHistory.objects.filter(user=user, bike=bike, return_time__isnull=True).last()
        if user_history is None:
            raise serializers.ValidationError("You already returned the bike.")

        latitude = attrs.get("latitude")
        longitude = attrs.get("longitude")
        bike.location = "%s,%s" % (latitude, longitude)
        bike.save()

        route_line = attrs.get("route_line")
        route_line_history = json.loads(user_history.route_line)
        route_line_history += route_line
        user_history.route_line = json.dumps(route_line_history)
        user_history.save()

        total_duration = (timezone.now() - user_history.borrow_time).total_seconds()
        if total_duration <= user_history.selected_plan.period:
            return {"overdue": False}
        return {"overdue": True,
                "minutes_overdue": total_duration // 60}


class UpdateBikeLocationView(AbstractAPIView):

    serializer_class = UpdateBikeLocationSerializer

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
    return UpdateBikeLocationView.as_view()
