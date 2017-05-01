from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.status import *

from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView
from reports.models import Report


class GetReportTypeView(AbstractAPIView):

    @method_decorator(token_required)
    def get(self, request):
        data = []
        for type_id, type_name in Report.get_type():
            data.append({"id": type_id, "name": type_name})
        return Response(data, status=HTTP_200_OK)


def as_view():
    return GetReportTypeView.as_view()
