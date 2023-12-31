# Generated by Django 3.1.14 on 2022-01-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0204_feedback2fromintern_feedback2frommentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='inclusive_participation',
            field=models.TextField(blank=True, max_length=3000, verbose_name='How do people impacted by your work participate in your community?'),
        ),
        migrations.AddField(
            model_name='community',
            name='open_science_community',
            field=models.BooleanField(default=False, verbose_name='Is your community an open science community?'),
        ),
        migrations.AddField(
            model_name='community',
            name='open_science_funder_questions',
            field=models.TextField(blank=True, max_length=3000),
        ),
        migrations.AddField(
            model_name='community',
            name='open_science_practices',
            field=models.TextField(blank=True, max_length=3000, verbose_name='How does your community implement reproducible research, open access, open data sets, open data science, open collaboration, citizen science, or open source software?'),
        ),
    ]
