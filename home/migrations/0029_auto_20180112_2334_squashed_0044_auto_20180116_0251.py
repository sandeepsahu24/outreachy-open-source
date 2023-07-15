# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-16 18:17
from __future__ import unicode_literals

import ckeditor.fields
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_refactor_approval_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinatorapproval',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='mentorapproval',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='list_community',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='reason_for_not_participating',
        ),
        migrations.RemoveField(
            model_name='project',
            name='list_project',
        ),
        migrations.AlterField(
            model_name='comrade',
            name='pronouns',
            field=models.CharField(choices=[('she', 'she/her/her'), ('he', 'he/him/him'), ('they', 'they/them/their'), ('fae', 'fae/faer/faer'), ('ey', 'ey/em/eir'), ('per', 'per/per/pers'), ('ve', 've/ver/vis'), ('xe', 'xem/xyr/xyrs'), ('ze', 'hir/hir/hirs')], default=['they', 'them', 'their', 'theirs', 'themself', 'http://pronoun.is/they'], help_text="Your preferred pronoun. This will be used in emails from Outreachy organizers directly to you. The format is subject/object/possessive. Example: '__(subject)__ interned with Outreachy. The mentor liked working with __(object)__. __(possessive)__ internship project was challenging.", max_length=4, verbose_name='Pronouns'),
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='communication_channel_username',
            field=models.CharField(blank=True, help_text='What is your username on the team communication channel? (This information will be shared with applicants.)', max_length=100),
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='longevity',
            field=models.CharField(choices=[('3M', '0-2 months'), ('6M', '3-5 months'), ('1Y', '6-11 months'), ('2Y', '1-2 years'), ('OL', 'More than 2 years')], default='3M', help_text='How long have you been a contributor on this team?', max_length=2),
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='understands_applicant_time_commitment',
            field=models.BooleanField(default=False, help_text='I understand that Outreachy mentors often find they must spend more time helping applicants during the application period than helping their intern during the internship period'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='community_size',
            field=models.CharField(choices=[('3', '1-2 people'), ('5', '3-5 people'), ('10', '6-10 people'), ('20', '11-20 people'), ('50', '21-50 people'), ('100', '50-100 people'), ('999', 'More than 100 people')], default='3', help_text='How many people are contributing to this FOSS community regularly?', max_length=3),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='longevity',
            field=models.CharField(choices=[('3M', '0-2 months'), ('6M', '3-5 months'), ('1Y', '6-11 months'), ('2Y', '1-2 years'), ('OL', 'More than 2 years')], default='3M', help_text='How long has this FOSS community accepted public contributions?', max_length=2),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='participating_orgs',
            field=models.CharField(help_text='What different organizations and companies participate in this FOSS community?', max_length=3000),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='unapproved_license_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) If your FOSS community uses a license that is not an OSI-approved and FSF-approved license OR a Creative Commons license, please provide a description and links to the non-free licenses.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='accepting_new_applicants',
            field=models.BooleanField(default=True, help_text='Is this internship project currently accepting contributions from new applicants? If you have an applicant in mind to accept as an intern (or several promising applicants) who have filled out the eligibility information and an application, you can uncheck this box to close the internship project to new applicants.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='approved_license',
            field=models.BooleanField(default=False, help_text='I assert that this Outreachy internship project will released under either an <a href="https://opensource.org/licenses/alphabetical">OSI-approved open source license</a> that is also identified by the FSF as a <a href="https://www.gnu.org/licenses/license-list.html">free software license</a>, OR a <a href="https://creativecommons.org/share-your-work/public-domain/freeworks/">Creative Commons license approved for free cultural works</a>'),
        ),
        migrations.RemoveField(
            model_name='project',
            name='communication_help',
        ),
        migrations.RemoveField(
            model_name='project',
            name='communication_norms',
        ),
        migrations.RemoveField(
            model_name='project',
            name='communication_url',
        ),
        migrations.AlterField(
            model_name='project',
            name='community_benefits',
            field=models.CharField(blank=True, help_text='How will this internship project benefit the FOSS community that is funding it?', max_length=800),
        ),
        migrations.AlterField(
            model_name='project',
            name='community_size',
            field=models.CharField(choices=[('3', '1-2 people'), ('5', '3-5 people'), ('10', '6-10 people'), ('20', '11-20 people'), ('50', '21-50 people'), ('100', '50-100 people'), ('999', 'More than 100 people')], default='3', help_text='How many regular contributors does this team have?', max_length=3),
        ),
        migrations.AlterField(
            model_name='project',
            name='issue_tracker',
            field=models.URLField(blank=True, help_text="(Optional) URL for your team's issue tracker"),
        ),
        migrations.AlterField(
            model_name='project',
            name='long_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Description of the internship project, excluding applicant skills.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='longevity',
            field=models.CharField(choices=[('3M', '0-3 months'), ('6M', '3-6 months'), ('1Y', '6-12 months'), ('2Y', '1-2 years'), ('OL', 'More than 2 years')], default='3M', help_text="How long has the team accepted publicly submitted contributions? (See the 'Terms Used' section above for a definition of a team.", max_length=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='newcomer_issue_tag',
            field=models.CharField(blank=True, help_text='(Optional) What tag is used for newcomer-friendly issues for your team or for this internship project?', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='repository',
            field=models.URLField(blank=True, help_text="(Optional) URL for your team's repository or contribution mechanism"),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_title',
            field=models.CharField(help_text='Short title for this internship project proposal. This should be 100 characters or less, starting with a verb like "Create", "Improve", "Extend", "Survey", "Document", etc. Assume the applicant has never heard of your technology before and keep it simple. The short title will be used in your project page URL, so keep it short.', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(verbose_name='Project URL slug'),
        ),
        migrations.AlterField(
            model_name='projectskill',
            name='experience_level',
            field=models.CharField(choices=[('WTU', 'Mentors are willing to teach this skill to applicants with no experience at all'), ('CON', 'Applicants should have read about the skill'), ('EXP', 'Applicants should have used this skill in class or personal projects'), ('FAM', 'Applicants should be able to expand on their skills with the help of mentors'), ('CHA', 'Applicants who are experienced in this skill will have the chance to expand it further')], default='WTU', help_text='Choose this carefully! Many Outreachy applicants choose not to apply for an internship project unless they meet 100% of the project skill criteria.', max_length=3, verbose_name='Expected skill experience level'),
        ),
        migrations.AlterField(
            model_name='projectskill',
            name='required',
            field=models.CharField(choices=[('BON', 'It would be nice if applicants had this skill, but it will not impact intern selection'), ('OPT', 'Mentors will prefer applicants who have this skill'), ('STR', 'Mentors will only accept applicants who have this skill as an intern')], default='BON', help_text='Is this skill a hard requirement, a preference, or an optional bonus? Choose this carefully! Many Outreachy applicants choose not to apply for an internship project unless they meet 100% of the project skill criteria.', max_length=3, verbose_name='Skill impact on intern selection'),
        ),
        migrations.AlterField(
            model_name='projectskill',
            name='skill',
            field=models.CharField(help_text='What is one skill an the applicant needs to have in order to contribute to this internship project, or what skill will they need to be willing to learn?', max_length=100, verbose_name='Skill description'),
        ),
        migrations.AlterField(
            model_name='coordinatorapproval',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('W', 'Withdrawn'), ('R', 'Rejected')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('W', 'Withdrawn'), ('R', 'Rejected')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='participation',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('W', 'Withdrawn'), ('R', 'Rejected')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('W', 'Withdrawn'), ('R', 'Rejected')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='longevity',
            field=models.CharField(choices=[('3M', '0-2 months'), ('6M', '3-5 months'), ('1Y', '6-11 months'), ('2Y', '1-2 years'), ('OL', 'More than 2 years')], default='3M', help_text="How long has the team accepted publicly submitted contributions? (See the 'Terms Used' section above for a definition of a team.", max_length=2),
        ),
        migrations.CreateModel(
            name='CommunicationChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(help_text='Name of the communication tool your project uses. E.g. "a mailing list", "IRC", "Zulip", "Mattermost", or "Discourse"', max_length=100)),
                ('url', models.CharField(help_text='URL for the communication channel applicants will use to reach mentors and ask questions about this internship project. IRC URLs should be in the form irc://<host>[:port]/[channel]. Since many applicants have issues with IRC port blocking at their universities, IRC communication links will use <a href="https://kiwiirc.com/">Kiwi IRC</a> to direct applicants to a web-based IRC client. If this is a mailing list, the URL should be the mailing list subscription page.', max_length=200, validators=[django.core.validators.URLValidator(schemes=['http', 'https', 'irc'])])),
                ('instructions', ckeditor.fields.RichTextField(blank=True, help_text='(Optional) After following the communication channel link, are there any special instructions? For example: "Join the #outreachy channel and make sure to introduce yourself.')),
                ('norms', ckeditor.fields.RichTextField(blank=True, help_text="(Optional) What communication norms would a newcomer need to know about this communication channel? Example: newcomers to open source don't know they should Cc their mentor or the software maintainer when asking a question to a large mailing list. Think about what a newcomer would find surprising when communicating on this channel.")),
                ('communication_help', models.URLField(blank=True, help_text='(Optional) URL for the documentation for your communication tool. This should be user-focused documentation that explains the basic mechanisms of logging in and features. Suggestions: IRC - https://wiki.gnome.org/Outreachy/IRC; Zulip - https://chat.zulip.org/help/; Mattersmost - https://docs.mattermost.com/guides/user.html')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='communication_tool',
        ),
        migrations.AlterField(
            model_name='project',
            name='long_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Description of the internship project, excluding applicant skills and communication channels. Those will be added in the next step.'),
        ),
        migrations.AddField(
            model_name='communicationchannel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Project'),
        ),
        migrations.AddField(
            model_name='mentorapproval',
            name='mentor_foss_contributions',
            field=models.CharField(default='No contributions to either the team or the FOSS community', help_text='What contributions have you made to this team and the FOSS community who is funding this internship? If none, what contributions have you made to other FOSS communities?', max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentorapproval',
            name='mentorship_style',
            field=models.CharField(default="I don't know what my mentorship style is", help_text='What is your mentorship style? Do you prefer short daily standups, longer weekly reports, or informal progress reports? Are you willing to try pair programming when your intern gets stuck? Do you like talking over video chat or answering questions via email? Give the applicants a sense of what it will be like to work with you during the internship.', max_length=800),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='participating_orgs',
            field=models.CharField(help_text='What different organizations and companies participate in this FOSS community? If there are many organizations, list the top five organizations who make large contributions.', max_length=3000),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_signup', models.DateField(auto_now_add=True, verbose_name='Date user signed up for notifications')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Community')),
                ('comrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Comrade')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='notification',
            unique_together=set([('community', 'comrade')]),
        ),
        migrations.RemoveField(
            model_name='participation',
            name='cfp_text',
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='instructions_read',
            field=models.BooleanField(default=False, help_text='I have read the <a href="/mentor/#mentor">mentor duties</a> and <a href="/mentor/mentor-faq/">mentor FAQ</a>.', validators=[home.models.mentor_read_instructions]),
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='understands_applicant_time_commitment',
            field=models.BooleanField(default=False, help_text='I understand that Outreachy mentors often find they must spend more time helping applicants during the application period than helping their intern during the internship period', validators=[home.models.mentor_read_instructions]),
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='understands_intern_time_commitment',
            field=models.BooleanField(default=False, help_text='I understand that Outreachy mentors will spend a minimum of 5 hours a week mentoring their intern during the three month internship period', validators=[home.models.mentor_read_instructions]),
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='understands_mentor_contract',
            field=models.BooleanField(default=False, help_text='I understand that Outreachy mentors will need to sign a <a href="/documents/1/Outreachy-Program--Mentorship-Terms-of-Participation-May-2017.pdf">mentor contract</a> after they accept an applicant as an intern', validators=[home.models.mentor_read_contract]),
        ),
        migrations.AddField(
            model_name='project',
            name='intern_tasks',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) Description of possible internship tasks.', max_length=800),
        ),
        migrations.AlterField(
            model_name='project',
            name='community_benefits',
            field=models.CharField(blank=True, help_text='(Optional) How will this internship project benefit the FOSS community that is funding it?', max_length=800),
        ),
        migrations.AlterField(
            model_name='project',
            name='intern_benefits',
            field=models.CharField(blank=True, help_text="(Optional) How will the intern benefit from working with your team on this project? Imagine you're pitching this internship to a promising candidate. What would you say to convince them to apply? For example, what technical and non-technical skills will they learn from working on this project? How will this help them further their career in open source?", max_length=800),
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinator_can_update', models.BooleanField(help_text='\n            Can a community coordinator update this information, or is\n            it provided by the Outreachy organizers?\n            ')),
                ('name', models.CharField(help_text='The full sponsor name to be used on invoices.', max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('funding_secured', models.BooleanField(default=False, help_text='\n            Is this funding confirmed by the sponsoring organization, or\n            is it currently only tentative?\n            ')),
                ('funding_decision_date', models.DateField(default=datetime.date.today, help_text='Date by which you will know if this funding is confirmed.')),
                ('additional_information', ckeditor.fields.RichTextField(blank=True, help_text='\n            Anything else the Outreachy organizers should know about\n            this sponsorship.\n            ')),
            ],
        ),
        migrations.RemoveField(
            model_name='participation',
            name='interns_funded',
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='participation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Participation'),
        ),
        migrations.AlterField(
            model_name='communicationchannel',
            name='url',
            field=models.CharField(help_text='URL for the communication channel applicants will use to reach mentors and ask questions about this internship project. IRC URLs should be in the form irc://&lt;host&gt;[:port]/[channel]. Since many applicants have issues with IRC port blocking at their universities, IRC communication links will use <a href="https://kiwiirc.com/">Kiwi IRC</a> to direct applicants to a web-based IRC client. If this is a mailing list, the URL should be the mailing list subscription page.', max_length=200, validators=[django.core.validators.URLValidator(schemes=['http', 'https', 'irc'])]),
        ),
        migrations.AlterField(
            model_name='project',
            name='community_benefits',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) How will this internship project benefit the FOSS community that is funding it?', max_length=800),
        ),
        migrations.AlterField(
            model_name='project',
            name='intern_benefits',
            field=ckeditor.fields.RichTextField(blank=True, help_text="(Optional) How will the intern benefit from working with your team on this project? Imagine you're pitching this internship to a promising candidate. What would you say to convince them to apply? For example, what technical and non-technical skills will they learn from working on this project? How will this help them further their career in open source?", max_length=800),
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='mentored_before',
            field=models.CharField(choices=[('OUT', 'Yes, I have mentored in a past Outreachy round'), ('GSOC', 'No, but I have mentored for Google Summer of Code or Google Code In'), ('RAILS', 'No, but I have mentored for Rails Girls Summer of Code'), ('UNK', 'No, but I have mentored with another mentorship program'), ('NOT', 'No, I have never mentored before')], default='NOT', help_text='Have you been a mentor for Outreachy before? (Note that Outreachy welcomes first time mentors, but this information allows the coordinator and other mentors to provide extra help to new mentors.)', max_length=5),
        ),
    ]