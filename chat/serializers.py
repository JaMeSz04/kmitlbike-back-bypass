import json

from django.utils import timezone
from rest_framework import serializers

from chat.models import *


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "text", "status", "datetime", "type", "sender")


class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messenger
        fields = ("id", "room_name", "message")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "room_name", "user")
