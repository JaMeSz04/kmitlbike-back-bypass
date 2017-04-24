import json

from django.http import HttpResponse
from rest_framework.status import *

from bikes.models import Bike
from kmitl_bike_django.decorators import token_required


class BikesAPI(object):

    @staticmethod
    @token_required
    def get_available_bikes(request):
        if request.method == "GET":
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

    @staticmethod
    @token_required
    def borrow_bike(request, bike_id=None):
        if request.method == "GET":
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

    @staticmethod
    @token_required
    def return_bike(request, bike_id=None):
        if request.method == "GET":
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

    @staticmethod
    @token_required
    def update_bike_location(request, bike_id=None):
        if request.method == "POST":
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")
