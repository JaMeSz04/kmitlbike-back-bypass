# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 09:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PointTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('point', models.IntegerField(verbose_name=b'Point')),
                ('transaction_type', models.IntegerField(choices=[(1, b'Initial'), (2, b'Deposit'), (3, b'Refund'), (4, b'Penalty'), (5, b'Special')], verbose_name=b'Transaction type')),
                ('comment', models.CharField(blank=True, max_length=255, verbose_name=b'Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Point Transaction',
                'verbose_name_plural': 'Point Transactions',
            },
        ),
        migrations.CreateModel(
            name='UserExtraProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('kmitl_id', models.CharField(blank=True, max_length=32, verbose_name=b'KMITL ID')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name=b'First name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name=b'Last name')),
                ('id_card', models.CharField(blank=True, max_length=255, verbose_name=b'ID card')),
                ('phone_no', models.CharField(blank=True, max_length=32, verbose_name=b'Phone no.')),
                ('faculty', models.CharField(blank=True, max_length=255, verbose_name=b'Faculty')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name=b'Email')),
                ('forward_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name=b'Forward email')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile (Extra)',
                'verbose_name_plural': "Users' Profiles (Extra)",
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('gender', models.IntegerField(choices=[(1, b'Male'), (2, b'Female'), (3, b'Other')], verbose_name=b'Gender')),
                ('phone_no', models.CharField(max_length=32, verbose_name=b'Phone no.')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': "Users' Profiles",
            },
        ),
    ]
