from django.utils.decorators import method_decorator
from rest_framework.exceptions import AuthenticationFailed, NotFound
from rest_framework.response import Response
from rest_framework.status import *

from histories.models import UserHistory
from histories.serializers import UserHistorySerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class GetUserHistoryView(AbstractAPIView):

    serializer_class = UserHistorySerializer

    @method_decorator(token_required)
    def get(self, request, user_id=None, hist_id=None):
        if int(user_id) is request.user.id:
            try:
                user_history = UserHistory.objects.get(id=hist_id)
                data = self.serializer_class(user_history).data
                return Response(data, status=HTTP_200_OK)
            except UserHistory.DoesNotExist:
                raise NotFound("User history does not exist.")
        raise AuthenticationFailed()
