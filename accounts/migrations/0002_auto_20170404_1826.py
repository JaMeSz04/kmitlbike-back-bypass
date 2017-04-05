# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrauserprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='extrauserprofile',
            name='faculty',
            field=models.CharField(blank=True, max_length=255, verbose_name='Faculty'),
        ),
        migrations.AlterField(
            model_name='extrauserprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='extrauserprofile',
            name='forward_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Forward email'),
        ),
        migrations.AlterField(
            model_name='extrauserprofile',
            name='id_card',
            field=models.CharField(blank=True, max_length=255, verbose_name='ID card'),
        ),
        migrations.AlterField(
            model_name='extrauserprofile',
            name='kmitl_id',
            field=models.CharField(blank=True, max_length=32, verbose_name='KMITL ID'),
        ),
        migrations.AlterField(
            model_name='extrauserprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='extrauserprofile',
            name='phone_no',
            field=models.CharField(blank=True, max_length=32, verbose_name='Phone no.'),
        ),
    ]
