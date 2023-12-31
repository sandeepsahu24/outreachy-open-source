# Generated by Django 3.1.6 on 2021-07-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0199_auto_20210601_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcommunity',
            name='licenses_used',
            field=models.TextField(blank=True, help_text='For each repository listed above, say which open source license they use.', max_length=3000, verbose_name='List of open source licenses used'),
        ),
        migrations.AddField(
            model_name='newcommunity',
            name='repositories',
            field=models.TextField(blank=True, help_text="List the URLs of community repositories. Repositories can contain your open source community's code, documentation, and/or creative works. Repositories are usually hosted on GitHub, GitLab, or community web servers. If your community has multiple repositories, list the repositories which Outreachy applicants and interns will be likely to interact with.", max_length=3000, verbose_name='List of repositories'),
        ),
    ]
