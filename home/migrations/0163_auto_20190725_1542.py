# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-25 15:42
from __future__ import unicode_literals

from django.db import migrations
import datetime
from home.models import get_deadline_date_for

def update_rounds(apps, schema_editor):
    RoundPage = apps.get_model('home.RoundPage')
    rounds = RoundPage.objects.all()
    for r in rounds:
        outreachy_chat_date = r.initial_applications_open + datetime.timedelta(days=14)
        r.outreachy_chat = datetime.datetime(year=outreachy_chat_date.year, month=outreachy_chat_date.month, day=outreachy_chat_date.day, hour=16, tzinfo=datetime.timezone.utc)
        r.save()

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0162_auto_20190725_1542'),
    ]

    operations = [
        migrations.RunPython(update_rounds, reverse_code=migrations.RunPython.noop),
    ]
