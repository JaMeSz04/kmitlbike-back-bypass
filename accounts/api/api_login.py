from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.status import *

from accounts.backends import KMITLBackend


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        ser
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # result, token = KMITLBackend.authenticate(username, password)
        # if result == "exists":
        #     if token:
        #         user = token.user
        #         if user.is_active:
        #             response = {"result": "exists",
        #                         "token": str(token),
        #                         "first_name": user.first_name,
        #                         "last_name": user.last_name,
        #                         "gender": user.gender,
        #                         "email": user.email,
        #                         "phone_no": user.phone_no}
        #             return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        #         else:
        #             response = {"result": "banned"}
        #             return HttpResponse(json.dumps(response), status=HTTP_401_UNAUTHORIZED,
        #                                 content_type="application/json")
        # elif result == "first_time":
        #     response = {"result": "first_time"}
        #     return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        # response = {"result": "denied"}
        return HttpResponse(json.dumps(response), status=HTTP_401_UNAUTHORIZED, content_type="application/json")
    else:
        return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")