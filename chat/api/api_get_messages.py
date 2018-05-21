from rest_framework.mixins import ListModelMixin

from chat.models import Message
from chat.serializers import MessageSerializer
from kmitl_bike_django.utils import AbstractAPIView


class GetMessagesView(AbstractAPIView, ListModelMixin):
    serializer_class = MessageSerializer
    queryset = Message.objects.filter(status=2)

    # @method_decorator(token_required)
    def get(self, request):
        return self.list(request)


def as_view():
    return GetMessagesView.as_view()
