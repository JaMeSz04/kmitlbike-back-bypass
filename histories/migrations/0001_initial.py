# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 08:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bikes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('borrow_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Borrow time')),
                ('return_time', models.DateTimeField(blank=True, null=True, verbose_name=b'Return time')),
                ('route_line', models.TextField(default=b'[]', verbose_name=b'Route line')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.Bike')),
                ('selected_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.BikeUsagePlan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "User's History",
                'verbose_name_plural': "User's Histories",
            },
        ),
    ]
