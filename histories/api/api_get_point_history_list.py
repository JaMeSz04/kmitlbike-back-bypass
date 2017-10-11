from django.utils.decorators import method_decorator
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.mixins import ListModelMixin

from accounts.models import PointTransaction
from accounts.serializers import PointTransactionSerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class GetPointHistoryListView(AbstractAPIView, ListModelMixin):

    serializer_class = PointTransactionSerializer

    @method_decorator(token_required)
    def get(self, request, user_id):
        if int(user_id) is request.user.id:
            self.queryset = PointTransaction.objects.filter(user_id=user_id).order_by("-created_date")
            return self.list(request)
        raise AuthenticationFailed()


def as_view():
    return GetPointHistoryListView.as_view()
