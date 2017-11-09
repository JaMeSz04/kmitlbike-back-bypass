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

    payload = models.TextField("Payload", null=False, blank=False)
    status = models.IntegerField("Status", null=False, blank=False, choices=_status)
    send_time = models.DateTimeField("Send time", auto_now_add=True, null=False, blank=False)
    type = models.IntegerField("Type", null=False, blank=False, choices=_type)
    sender = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.payload)


class Messenger(AbstractModel):
    class Meta:
        verbose_name = "Messenger"
        verbose_name_plural = "Messengers"

    user_id = models.TextField(User, null=False, blank=False)
    message_id = models.TextField(Message, null=False, blank=False)
