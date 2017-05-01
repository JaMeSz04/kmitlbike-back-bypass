from django.utils.decorators import method_decorator
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import *

from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView
from reports.serializers import FeedbackSerializer


class SendFeedbackView(AbstractAPIView, CreateModelMixin):

    serializer_class = FeedbackSerializer

    @method_decorator(token_required)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            data["user"] = request.user
            serializer.create(data)
            return Response(status=HTTP_200_OK)
        error_message = self.get_error_message(serializer.errors)
        return Response({"detail": error_message}, status=HTTP_400_BAD_REQUEST)


def as_view():
    return SendFeedbackView.as_view()
