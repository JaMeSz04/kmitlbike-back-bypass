from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.status import *

from histories.models import UserHistory
from histories.serializers import UserHistorySerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class GetUserSessionView(AbstractAPIView):

    serializer_class = UserHistorySerializer

    @method_decorator(token_required)
    def get(self, request, user_id=None):
        user_history = UserHistory.objects.filter(user=request.user, return_time__isnull=True).last()
        if user_history is None:
            return Response({"resume": False}, status=HTTP_200_OK)
        data = self.get_serializer(user_history).data
        data["resume"] = True
        return Response(data, status=HTTP_200_OK)