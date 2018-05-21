from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.status import *

from histories.models import UserHistory
from histories.serializers import UserHistorySerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView

from django.utils import timezone

from operation_day.models import OperationDays, Holidays
from operation_day.serializers import OperationDaysSerialzer, HolidaysSerializers


class GetUserSessionView(AbstractAPIView):

    serializer_class = UserHistorySerializer

    #@method_decorator(token_required)
    def get(self, request, user_id=None):
        user_history = UserHistory.objects.filter(user=request.user, return_time__isnull=True).last()
        if user_history is None:
            return Response({"resume": False,
                             "operating": operation_day(),
                             }, status=HTTP_200_OK)
        data = self.get_serializer(user_history).data
        data["resume"] = True
        data["operating"] = operation_day()
        return Response(data, status=HTTP_200_OK)


def operation_day():
    now = timezone.localtime()
    day = now.weekday()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    operation = OperationDays.objects.get(day=days[day])

    return ({"start_time": operation.open_time,
             "close_time": operation.open_time,
             "is_available": operation.is_operated,
             "holiday": get_holiday()})


def get_holiday():
    now = timezone.localtime()
    today = now.date()

    holiday = Holidays.objects.filter(date=today)
    if not holiday:
        return "null"
    return str(holiday[0].day)


def as_view():
    return GetUserSessionView.as_view()







