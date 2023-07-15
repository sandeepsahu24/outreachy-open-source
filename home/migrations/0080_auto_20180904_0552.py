# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-04 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0079_priorfossexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priorfossexperience',
            name='gsoc_or_outreachy_internship',
            field=models.BooleanField(help_text='Please say yes even if you did not successfully complete the internship.', verbose_name='Have you been accepted as a Google Summer of Code intern, an Outreach Program for Women intern, or an Outreachy intern before?'),
        ),
        migrations.AlterField(
            model_name='priorfossexperience',
            name='prior_contributor',
            field=models.BooleanField(help_text='<p>Outreachy welcomes applicants who are newcomers to free and open source software (FOSS). We also welcome applicants who have made contributions to FOSS, and want to take the next step in their FOSS career. Outreachy asks this questions to see if we are meeting our goal of promoting free software to people from groups under-represented in the technology industry. It will not have an impact on your initial application approval.</p><p>Please exclude contributions that were made as part of a prior Outreachy application period.</p>', verbose_name='Have you contributed to free and open source software before?'),
        ),
        migrations.AlterField(
            model_name='priorfossexperience',
            name='prior_paid_contributor',
            field=models.BooleanField(help_text='Please include paid internships, contract work, employment, stipends, or grants.', verbose_name='Have you ever been PAID to contribute to free and open source software before?'),
        ),
    ]
