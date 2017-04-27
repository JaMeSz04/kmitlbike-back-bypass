from django.http import HttpResponse
from rest_framework.status import *

from kmitl_bike_django.decorators import token_required


@token_required
def update_bike_location(request, bike_id=None):
    if request.method == "POST":
        return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
    else:
        return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")
