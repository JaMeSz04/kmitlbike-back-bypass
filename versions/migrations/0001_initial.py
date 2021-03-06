# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 08:45
from __future__ import unicode_literals

from django.db import migrations, models


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
                ('platform', models.CharField(choices=[(b'android', b'Andriod'), (b'ios', b'iOS')], max_length=8, verbose_name=b'Platform')),
                ('version_code', models.CharField(max_length=32, verbose_name=b'Version code')),
                ('version_name', models.CharField(blank=True, max_length=32, verbose_name=b'Version name')),
                ('url', models.URLField(verbose_name=b'URL')),
            ],
            options={
                'verbose_name': 'Mobile Application Version',
                'verbose_name_plural': 'Mobile Application Versions',
            },
        ),
        migrations.AlterUniqueTogether(
            name='appversion',
            unique_together=set([('platform', 'version_code')]),
        ),
        migrations.CreateModel(
            name='AndroidAppVersion',
            fields=[
            ],
            options={
                'verbose_name': 'Android Application Version',
                'proxy': True,
                'verbose_name_plural': 'Android Application Versions',
                'indexes': [],
            },
            bases=('versions.appversion',),
        ),
        migrations.CreateModel(
            name='IosAppVersion',
            fields=[
            ],
            options={
                'verbose_name': 'iOS Application Version',
                'proxy': True,
                'verbose_name_plural': 'iOS Application Versions',
                'indexes': [],
            },
            bases=('versions.appversion',),
        ),
    ]
