from django.utils.decorators import method_decorator
from rest_framework.mixins import ListModelMixin

from kmitl_bike_django.decorators import  token_required
from kmitl_bike_django.utils import AbstractAPIView

from chat.models import Message
from chat.serializers import MessageSerializer


class GetUnreadMessagesView(AbstractAPIView, ListModelMixin):

    serializer_class = MessageSerializer
    queryset = Message.objects.filter(status=2)

    #@method_decorator(token_required)
    def get(self, request):
        return self.list(request)


def as_view():
    return GetUnreadMessagesView.as_view()