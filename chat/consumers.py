from channels import Group
from channels.sessions import channel_session
from chat.models import *


@channel_session
def ws_add(message, room):
    # Group('chat').add(message.reply_channel)
    Group('chat-%s' %room).add(message.reply_channel)
    message.channel_session['room'] = room
    message.reply_channel.send({"accept" : True})





@channel_session
def ws_echo(message):
    print(message)
    print(message.content)
    print(message.content['text'])
    room = message.channel_session['room']
    Group('chat-%s'%room).send({
        'text' : message.content['text'] + " from group : " + str(room)
    })

    #  message.reply_channel.send({
    #     'text' : message.content['text'],
    # })