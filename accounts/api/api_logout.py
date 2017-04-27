from django.http import HttpResponse
from rest_framework.status import *

from kmitl_bike_django.decorators import token_required


@token_required
def logout(request):
    if request.method == "GET":
        request.token.delete()
        return HttpResponse(status=HTTP_200_OK, content_type="application/json")
    else:
        return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")