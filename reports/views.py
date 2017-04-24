import json

from django.http import HttpResponse
from rest_framework.status import *

from kmitl_bike_django.decorators import token_required


class ReportsAPI(object):

    @staticmethod
    @token_required
    def send_report(request):
        if request.method == "POST":
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

    @staticmethod
    @token_required
    def send_feedback(request):
        if request.method == "POST":
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")
