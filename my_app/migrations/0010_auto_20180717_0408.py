# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-17 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_auto_20180716_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='profilepic',
            field=models.ImageField(blank=True, upload_to='profilePic'),
        ),
    ]