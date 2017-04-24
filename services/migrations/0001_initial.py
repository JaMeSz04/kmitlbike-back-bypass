# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('platform', models.CharField(max_length=8, verbose_name=b'Platform')),
                ('version_code', models.CharField(max_length=32, verbose_name=b'Version code')),
                ('version_name', models.CharField(max_length=32, verbose_name=b'Version name')),
            ],
            options={
                'verbose_name': 'Mobile Application Version',
                'verbose_name_plural': 'Mobile Application Versions',
            },
        ),
        migrations.CreateModel(
            name='AndroidAppVersion',
            fields=[
                ('appversion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.AppVersion')),
            ],
            options={
                'verbose_name': 'Android Application Version',
                'verbose_name_plural': 'Android Application Versions',
            },
            bases=('services.appversion',),
        ),
        migrations.CreateModel(
            name='IosAppVersion',
            fields=[
                ('appversion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.AppVersion')),
            ],
            options={
                'verbose_name': 'iOS Application Version',
                'verbose_name_plural': 'iOS Application Versions',
            },
            bases=('services.appversion',),
        ),
    ]