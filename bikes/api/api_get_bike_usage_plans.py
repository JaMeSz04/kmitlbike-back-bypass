from django.utils.decorators import method_decorator
from rest_framework.mixins import ListModelMixin

from bikes.models import BikeUsagePlan
from bikes.serializers import BikeUsagePlanSerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class GetBikeUsagePlansView(AbstractAPIView, ListModelMixin):

    serializer_class = BikeUsagePlanSerializer
    queryset = BikeUsagePlan.objects.all()

    @method_decorator(token_required)
    def get(self, request):
        return self.list(request)


def as_view():
    return GetBikeUsagePlansView.as_view()
