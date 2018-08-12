# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-16 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, b'Active'), (2, b'Inactive')], verbose_name=b'status')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.Bike')),
            ],
            options={
                'verbose_name': "Bike's Status",
                'verbose_name_plural': "Bikes' Status",
            },
        ),
    ]