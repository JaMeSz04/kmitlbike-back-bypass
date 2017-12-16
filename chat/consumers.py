from channels import Group
from channels.sessions import channel_session

from chat.models import *
from serializers import *


from rest_framework import serializers


# class WebSocketSerializer(serializers.Serializer):
#
#     def __init__(self, *args, **kwargs):
#         super(WebSocketSerializer,self).__init__(*args, **kwargs)
#
#     def validate(self, attrs):
#         user = self.context.get("user")
#



@channel_session
def ws_add(message, room):
    # Group('chat').add(message.reply_channel)
    Group('chat-%s' %room).add(message.reply_channel)
    message.channel_session['room'] = room
    message.reply_channel.send({"accept" : True})

    try:
        return Room.objects.get(room_name=room)
    except Room.DoesNotExist:
        room_serializer = RoomSerializer(data={"room_name": room,
                                               "user": "57090023"})
        if room_serializer.is_valid():
            room_serializer.save()

@channel_session
def ws_echo(message):

    print(message)
    print(message.content)
    print(message.content['text'])
    room = message.channel_session['room']
    Group('chat-%s'%room).send({
        'text': message.content['text'] + " from group : " + str(room)
    })

    # save message
    message_serializer = MessageSerializer(data={"text": message.content["text"],
                                                 "sender": str(room),
                                                 "type": 1,
                                                 "status": 1,
                                                 "datetime": 0})
    if message_serializer.is_valid():
        message_serializer.save()

    # save messenger
    msg_obj = Message.objects.order_by('datetime').reverse().filter(sender=str(room))[0]
    ms = Message.objects.get(id=msg_obj.id)
    messenger_serializer = MessengerSerializer(data={"room_name": str(room),
                                                     "message": ms.id})
    if messenger_serializer.is_valid():
        messenger_serializer.save()


    #  message.reply_channel.send({
    #     'text' : message.content['text'],
    # })