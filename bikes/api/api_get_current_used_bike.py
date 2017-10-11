from django.utils.decorators import method_decorator
from rest_framework.mixins import ListModelMixin

from bikes.models import Bike
from bikes.serializers import CurrentUsedBikeSerializer
from histories.models import UserHistory
from histories.serializers import UserHistorySerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView

class GetCurrentUsedBikesView(AbstractAPIView,ListModelMixin):
    serializer_class = CurrentUsedBikeSerializer
    queryset = UserHistory.objects.filter(return_time=None)

    #method_decorator(token_required)
    def get(self, request):
        return self.list(request)

def as_view():
    return GetCurrentUsedBikesView.as_view()
