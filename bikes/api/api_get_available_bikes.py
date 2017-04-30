from django.utils.decorators import method_decorator
from rest_framework.mixins import ListModelMixin

from bikes.models import Bike
from bikes.serializers import BikeSerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class GetAvailableBikesView(AbstractAPIView, ListModelMixin):

    serializer_class = BikeSerializer
    queryset = Bike.objects.filter(is_available=True)

    @method_decorator(token_required)
    def get(self, request):
        return self.list(request)
