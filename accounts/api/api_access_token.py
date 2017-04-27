from django.http import HttpResponse
from rest_framework.status import *


def access_token(request):
    if request.method == "POST":
        token = request.POST.get("token")
        try:
            token, _ = Token.objects.get_or_create(key=token)
            response = {"token": token.key}
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        except IntegrityError:
            return HttpResponse(status=HTTP_401_UNAUTHORIZED, content_type="application/json")
    else:
        return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")