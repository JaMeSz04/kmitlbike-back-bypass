# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('payload', models.TextField(verbose_name=b'Payload')),
                ('status', models.IntegerField(choices=[(1, b'Read'), (2, b'Unread')], verbose_name=b'Status')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Send time')),
                ('type', models.IntegerField(choices=[(1, b'String'), (2, b'Image')], verbose_name=b'Type')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
