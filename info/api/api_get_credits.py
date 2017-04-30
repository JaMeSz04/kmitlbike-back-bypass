from django.utils.decorators import method_decorator
from rest_framework.mixins import ListModelMixin

from info.models import Credit
from info.serializers import CreditSerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class GetCreditsView(AbstractAPIView, ListModelMixin):

    serializer_class = CreditSerializer
    queryset = Credit.objects.all().order_by("position__priority", "position__name", "name")

    @method_decorator(token_required)
    def get(self, request):
        return self.list(request)
