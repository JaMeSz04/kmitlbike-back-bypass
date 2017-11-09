import json

from django.utils import timezone
from rest_framework import serializers

from chat.models import Message
from chat.models import Messenger


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "payload", "status", "datetime", "type")


class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messenger
        fields = ("id", "user_id", "message_id")


