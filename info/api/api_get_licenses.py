from django.utils.decorators import method_decorator
from rest_framework.mixins import ListModelMixin

from info.models import License
from info.serializers import LicenseSerializer
from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class GetLicensesView(AbstractAPIView, ListModelMixin):

    serializer_class = LicenseSerializer
    queryset = License.objects.all().order_by("name")

    @method_decorator(token_required)
    def get(self, request):
        return self.list(request)


def as_view():
    return GetLicensesView.as_view()
