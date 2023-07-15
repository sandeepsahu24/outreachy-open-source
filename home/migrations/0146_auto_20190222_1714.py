# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-22 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0145_noncollegeschooltimecommitment_quit_on_acceptance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotiontracking',
            name='spread_the_word',
            field=models.CharField(choices=[('AISES', 'Job board - American Indian Science and Engineering Society'), ('BIT', 'Job board - Blacks in Tech'), ('GWC', 'Job board - Girls Who Code'), ('NAJ', 'Job board - Native American Jobs'), ('POCIT', 'Job board - People of Color in Tech'), ('WWC', 'Job board - Women Who Code'), ('HYP', 'Community - Hypatia Software'), ('LAIT', 'Community - Latinas in Tech group'), ('LGBTQ', 'Community - LGBTQ in Tech slack'), ('RC', 'Community - Recurse Center'), ('H4CK', 'Community - Trans*H4CK'), ('WITCH', 'Community - Women in Tech Chat slack'), ('WIL', 'Community - Women in Linux group'), ('TAPIA', 'Conference - Richard Tapia Conference'), ('CONF', 'Conference - other'), ('PRES', 'Presentation by an Outreachy organizer, mentor, or coordinator'), ('ALUM', 'From a former Outreachy intern'), ('MENT', 'From an Outreachy mentor'), ('TEACH', 'From a teacher'), ('STUD', 'From a classmate'), ('PAL', 'From a friend'), ('TWIT', 'From Twitter'), ('SEAR', 'Found Outreachy from a web search'), ('OTH', 'Other')], default='OTH', max_length=5, verbose_name='How did you find out about Outreachy? (This will only be displayed to Outreachy Organizers.)'),
        ),
    ]
