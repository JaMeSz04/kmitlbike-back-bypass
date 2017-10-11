from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.status import *

from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView


class LogoutView(AbstractAPIView):

    @method_decorator(token_required)
    def post(self, request):
        request.token.delete()
        return Response({"result": True}, status=HTTP_200_OK)


def as_view():
    return LogoutView.as_view()
