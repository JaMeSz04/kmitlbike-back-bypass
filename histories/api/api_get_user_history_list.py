from django.utils.decorators import method_decorator
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.mixins import ListModelMixin

from histories.models import UserHistory
from histories.serializers import UserHistoryListSerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class GetUserHistoryListView(AbstractAPIView, ListModelMixin):

    serializer_class = UserHistoryListSerializer

    @method_decorator(token_required)
    def get(self, request, user_id):
        if int(user_id) is request.user.id:
            self.queryset = UserHistory.objects.filter(user_id=user_id, return_time__isnull=False)
            return self.list(request)
        raise AuthenticationFailed()
