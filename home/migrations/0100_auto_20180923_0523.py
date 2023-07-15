# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-23 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0099_applicationreviewer_initialapplicationreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrierstoparticipation',
            name='lacking_representation',
            field=models.TextField(help_text="<p>Contributing to free and open source software takes some skill. You may have already learned some basic skills through university or college classes, specialized schools, online classes, online resources, or with a mentor, friend, family member or co-worker.</p><p>Does any of your learning environments have few people who share your identity or background? How did your identity or background differ from the majority of people in this learning environment?</p><p>Outreachy Organizers strongly encourage you to write your personal stories. We want you to know that we won't judge your writing style, grammar or spelling.</p>", verbose_name='Does your learning environment have few people who share your identity or background? Please provide details.'),
        ),
    ]
