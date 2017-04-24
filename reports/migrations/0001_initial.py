# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('like', models.BooleanField(verbose_name=b'Like')),
                ('comment', models.TextField(blank=True, verbose_name=b'Comment')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('report_type', models.IntegerField(verbose_name=b'Report type')),
                ('detail', models.TextField(blank=True, verbose_name=b'Report detail')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
    ]
