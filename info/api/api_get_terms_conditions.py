from django.http import HttpResponse
from django.template import loader
from rest_framework.status import *

from kmitl_bike_django.utils import AbstractAPIView


class GetTermsConditionsView(AbstractAPIView):

    def get(self, request):
        template = loader.get_template("terms_conditions.html")
        return HttpResponse(template.render(request), status=HTTP_200_OK)
