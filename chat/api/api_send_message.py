import json

from django.utils.decorators import method_decorator
from rest_framework.mixins import ListModelMixin
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import *

from chat.models import Message
from chat.models import Messenger
from chat.serializers import MessageSerializer

from kmitl_bike_django.decorators import token_required
from kmitl_bike_django.utils import AbstractAPIView

'''
class SendMessage(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super(SendMessage, self).__init__(*args, **kwargs)
        self.field
'''