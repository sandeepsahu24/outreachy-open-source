# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-29 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0106_auto_20180929_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolinformation',
            name='applicant_should_update',
            field=models.BooleanField(default=False),
        ),
    ]
