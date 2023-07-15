# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 22:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('home', '0006_auto_20170803_0249'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutreachyHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.RichTextField(default='<p>Outreachy provides three-month, paid, remote internships for people traditionally underrepresented in tech. Individual donors and corporate sponsors provide funding for the program, and interns are often hired by our sponsors! Interns work directly with mentors from Free and Open Source (FOSS) communities on projects ranging from programming, user experience, documentation, illustration and graphical design, and data science.</p><p>Outreachy internships are open internationally to women (cis and trans), trans men, and genderqueer people. Internships are also open to residents and nationals of the United States of any gender who are Black/African American, Hispanic/Latin@, American Indian, Alaska Native, Native Hawaiian, or Pacific Islander. We are planning to expand the program to more participants from underrepresented backgrounds in the future.</p><p>Outreachy internships run twice a year.</p>')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='roundpage',
            name='sponsordetails',
            field=wagtail.core.fields.RichTextField(default='<p>Outreachy is hosted by the <a href="https://sfconservancy.org/">Software Freedom Conservancy</a> with special support from Red Hat, GNOME, and <a href="http://otter.technology">Otter Tech</a>. We invite companies and free and open source communities to sponsor internships in the next round.</p>'),
        ),
    ]
