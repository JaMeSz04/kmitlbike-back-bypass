# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('bike_name', models.CharField(max_length=64, unique=True, verbose_name=b'Bike name')),
                ('mac_addr', models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name=b'MAC address')),
                ('serial_no', models.CharField(max_length=32, null=True, unique=True, verbose_name=b'Serial no.')),
                ('barcode', models.CharField(max_length=16, null=True, unique=True, verbose_name=b'Barcode')),
                ('is_available', models.BooleanField(default=True, verbose_name=b'Is available')),
                ('current_lat', models.CharField(max_length=64, verbose_name=b'Current latitude')),
                ('current_long', models.CharField(max_length=64, verbose_name=b'Current longitude')),
                ('passcode', models.CharField(max_length=32, verbose_name=b'Passcode')),
            ],
            options={
                'verbose_name': 'Bike',
                'verbose_name_plural': 'Bikes',
            },
        ),
        migrations.CreateModel(
            name='BikeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('model_name', models.CharField(max_length=255, unique=True, verbose_name=b'Model name')),
            ],
            options={
                'verbose_name': 'Bike Model',
                'verbose_name_plural': 'Bike Models',
            },
        ),
        migrations.CreateModel(
            name='BikeUsagePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('plan_name', models.CharField(max_length=255, verbose_name=b'Plan name')),
                ('period', models.IntegerField(verbose_name=b'Period (minutes)')),
                ('price', models.IntegerField(verbose_name=b'Price')),
            ],
            options={
                'verbose_name': 'Bike Usage Plan',
                'verbose_name_plural': 'Bike Usage Plans',
            },
        ),
        migrations.AddField(
            model_name='bike',
            name='bike_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.BikeModel'),
        ),
    ]
