# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-02 21:54
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
