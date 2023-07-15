# Generated by Django 3.1.5 on 2021-02-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0197_roundpage_outreachy_chat_timezone_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecommitmentsummary',
            name='contractor',
            field=models.BooleanField(help_text="A contractor is someone who is self-employed. Contractors have clients. They are not employees of their clients. Instead, they are paid for completing a project. After the project ends, the contractor is no longer working for the client. When in doubt, say 'No' to this question.", verbose_name='Will you be a contractor during the Outreachy internship period?'),
        ),
    ]
