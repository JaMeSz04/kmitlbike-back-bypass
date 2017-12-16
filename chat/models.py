from django.contrib.auth.models import User
from django.db import models

from kmitl_bike_django.utils import AbstractModel


class Message(AbstractModel):
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    class Status(object):
        READ = 1
        UNREAD = 2

    class Type(object):
        STRING = 1
        IMAGE = 2

    _status = (
        (Status.READ, "Read"),
        (Status.UNREAD, "Unread")
    )

    _type = (
        (Type.STRING, "String"),
        (Type.IMAGE, "Image")
    )

    text = models.TextField("text", null=False, blank=False)
    status = models.IntegerField("status", choices=_status)
    datetime = models.DateTimeField("datetime", auto_now_add=True)
    type = models.IntegerField("type", choices=_type)
    sender = models.TextField("sender", null=False, blank=False)

    def __str__(self):
        return str(self.text)


class Messenger(AbstractModel):
    class Meta:
        verbose_name = "Messenger"
        verbose_name_plural = "Messengers"

    room_name = models.TextField("room_name", null=False, blank=False)
    message = models.ForeignKey(Message, null=False, blank=False)


class Room(AbstractModel):
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Room"

    room_name = models.TextField("room_name", null=False, blank=False)
    user = models.TextField("user", null=False, blank=False)



