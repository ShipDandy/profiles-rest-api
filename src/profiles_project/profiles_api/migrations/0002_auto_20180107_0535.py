# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
