# Generated by Django 3.1.14 on 2022-01-28 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0205_auto_20220109_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='internselection',
            name='feedback3_due',
            field=models.DateField(blank=True, null=True, verbose_name='Date feedback #3 form is due'),
        ),
        migrations.AddField(
            model_name='internselection',
            name='feedback3_opens',
            field=models.DateField(blank=True, null=True, verbose_name='Date feedback #3 form opens'),
        ),
        migrations.AddField(
            model_name='roundpage',
            name='feedback3_due',
            field=models.DateField(blank=True, null=True, verbose_name='Date feedback #3 is due'),
        ),
        migrations.CreateModel(
            name='Feedback3FromMentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_edits', models.BooleanField()),
                ('ip_address', models.GenericIPAddressField()),
                ('last_contact', models.DateField(verbose_name='What was the last date you were in contact with your intern?')),
                ('mentors_report', models.TextField(verbose_name='Please provide a paragraph describing what support you are providing as an Outreachy mentor. This will be shared with Outreachy organizers and your community coordinator.')),
                ('full_time_effort', models.BooleanField(verbose_name='Do you believe your Outreachy intern is putting in a full-time, 40 hours a week effort into the internship?')),
                ('organizer_payment_approved', models.BooleanField(default=None, help_text='Outreachy organizers approve or do not approve to pay this intern.', null=True)),
                ('request_extension', models.BooleanField(help_text='Sometimes interns do not put in a full-time effort. In this case, one of the options is to delay payment of their stipend and extend their internship a specific number of weeks. You will be asked to re-evaluate your intern after the extension is done.', verbose_name='Does your intern need an extension?')),
                ('request_termination', models.BooleanField(help_text='Sometimes after several extensions, interns still do not put in a full-time effort. If you believe that your intern would not put in a full-time effort with a further extension, you may request to terminate the internship. The Outreachy organizers will be in touch to discuss the request.', verbose_name='Do you believe the internship should be terminated?')),
                ('mentor_answers_questions', models.BooleanField(verbose_name="Do you (or a co-mentor) answer the intern's questions within 10 hours?")),
                ('intern_asks_questions', models.BooleanField(verbose_name='Does the intern ask you (or a co-mentor) questions when stuck for more than 1 to 3 hours?')),
                ('mentor_support_when_stuck', models.BooleanField(verbose_name='Do you (or a co-mentor) offer more support if the intern is stuck?')),
                ('daily_stand_ups', models.BooleanField(verbose_name='Do you (or a co-mentor) have daily stand ups with the intern?')),
                ('meets_privately', models.BooleanField(verbose_name='Do you (or a co-mentor) meet privately with the intern?')),
                ('meets_over_phone_or_video_chat', models.BooleanField(verbose_name='Do you (or a co-mentor) meet with the intern over phone or video chat?')),
                ('intern_missed_meetings', models.BooleanField(verbose_name='Has the intern recently missed more than 2 meetings?')),
                ('talk_about_project_progress', models.BooleanField(verbose_name='Does the intern and you (or a co-mentor) talk about project progress at least 3 days a week?')),
                ('reviewed_original_timeline', models.BooleanField(verbose_name='Has the intern and you (or a co-mentor) reviewed the original project timeline?')),
                ('contribution_drafts', models.BooleanField(verbose_name='Does the intern share work-in-progress or draft contributions with mentor(s)?')),
                ('contribution_review', models.BooleanField(verbose_name='Do you (or a co-mentor) review intern contributions within 1 to 3 days?')),
                ('contribution_revised', models.BooleanField(verbose_name='Has your intern revised their contribution(s) based on feedback?')),
                ('mentor_shares_positive_feedback', models.BooleanField(verbose_name='Do you (or a co-mentor) give your intern praise and positive feedback?')),
                ('mentor_promoting_work_to_community', models.BooleanField(verbose_name="Do you (or a co-mentor) promote your intern's contributions within your open source community?")),
                ('mentor_promoting_work_on_social_media', models.BooleanField(verbose_name="Do you (or a co-mentor) promote your intern's contributions on social media?")),
                ('intern_blogging', models.BooleanField(verbose_name='Has the intern been creating blog posts?')),
                ('mentor_discussing_blog', models.BooleanField(verbose_name="Do you (or a co-mentor) discuss your intern's blog posts with them?")),
                ('mentor_promoting_blog_to_community', models.BooleanField(verbose_name="Do you (or a co-mentor) promote your intern's blog posts to your open source community?")),
                ('mentor_promoting_blog_on_social_media', models.BooleanField(verbose_name="Do you (or a co-mentor) promote your intern's blog posts on social media?")),
                ('mentor_introduced_intern_to_community', models.BooleanField(verbose_name='Did you (or a co-mentor) introduce your intern to your open source community?')),
                ('intern_asks_questions_of_community_members', models.BooleanField(verbose_name='Does your intern seek help from open source community members who are not their mentors?')),
                ('intern_talks_to_community_members', models.BooleanField(verbose_name='Does your intern have casual conversations with open source community members who are not their mentors?')),
                ('progress_report', models.TextField(verbose_name="Please provide a paragraph describing your intern's communication frequency with you, the intern's progress on their project, and the intern's interactions with your open source community. This will only be shown to Outreachy organizers, your community coordinators, and the Software Freedom Conservancy accounting staff.")),
                ('payment_approved', models.BooleanField(help_text='Please base your answer on whether your intern has put in a full-time, 40 hours a week effort. They should have established communication with you and other mentors, and have started learning how to tackle their first tasks. If you are going to ask for an internship extension, please say no to this question.', verbose_name='Should your Outreachy intern be paid the initial $1,000 payment?')),
                ('extension_date', models.DateField(blank=True, help_text="If you want to extend the internship, please pick a date when you will be asked to update your intern's initial feedback and authorize payment. Internships can be extended for up to five weeks. We don't recommend extending an internship for more than 1 week at initial feedback. Please leave this field blank if you are not asking for an extension.", null=True)),
                ('actions_requested', models.CharField(choices=[('PAYCONT', 'Pay the final intern stipend'), ('1WEEK', 'Extend the internship 1 week total'), ('2WEEK', 'Extend the internship 2 weeks total'), ('3WEEK', 'Extend the internship 3 weeks total'), ('4WEEK', 'Extend the internship 4 weeks total'), ('5WEEK', 'Extend the internship 5 weeks total'), ('TERMPAY', 'Terminate the internship contract, and pay the final intern stipend'), ('TERMNOPAY', 'Terminate the internship contract, and do NOT pay the final intern stipend'), ('DONTKNOW', "I don't know what action to recommend, please advise")], default='PAYCONT', max_length=9, verbose_name='What actions are you requesting Outreachy organizers to take, based on your feedback?')),
                ('intern_selection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.internselection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback3FromIntern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_edits', models.BooleanField()),
                ('ip_address', models.GenericIPAddressField()),
                ('last_contact', models.DateField(verbose_name='What was the last date you were in contact with your mentor?')),
                ('hours_worked', models.CharField(choices=[('5H', '5 hours'), ('10H', '10 hours'), ('15H', '15 hours'), ('20H', '20 hours'), ('25H', '25 hours'), ('30H', '30 hours'), ('35H', '35 hours'), ('40H', '40 hours'), ('45H', '45 hours'), ('50H', '50 hours'), ('55H', '55 hours'), ('60H', '60 hours')], help_text='Include time you spend researching questions, communicating with your mentor and the community, reading about the project and the community, working on skills you need in order to complete your tasks, and working on the tasks themselves. Please be honest about the number of hours you are putting in.', max_length=3, verbose_name='What is the average number of hours per week you spend on your Outreachy internship?')),
                ('time_comments', models.TextField(blank=True, help_text="(Optional) If you have not been working 40 hours a week, please let us know why. We want to support you, so let us know if there's anything we can do to help.", max_length=3000)),
                ('mentor_support', models.TextField(verbose_name='Please provide a paragraph describing how your mentor has (or has not) been helping you. This information will only be seen by Outreachy mentors. We want you to be honest with us if you are having trouble with your mentor, so we can help you get a better internship experience.')),
                ('share_mentor_feedback_with_community_coordinator', models.BooleanField(default=False, help_text='If you say yes, community coordinators will be able to see your comments and the data you provided about your mentor. This helps coordinators ensure mentors are responsive, coach mentors if they are not responsive, and collect metrics they can use to fund more Outreachy internships.', verbose_name='(Optional) Do you want us to share feedback about your mentor with community coordinators?')),
                ('mentor_answers_questions', models.BooleanField(verbose_name='Do your mentor(s) answer your questions within 10 hours?')),
                ('intern_asks_questions', models.BooleanField(verbose_name='Do you ask your mentor(s) questions when stuck for more than 1 to 3 hours?')),
                ('mentor_support_when_stuck', models.BooleanField(verbose_name='Do your mentor(s) offer more support if you are stuck?')),
                ('daily_stand_ups', models.BooleanField(verbose_name='Do you and your mentor(s) have daily stand ups?')),
                ('meets_privately', models.BooleanField(verbose_name='Do you and your mentor(s) meet privately?')),
                ('meets_over_phone_or_video_chat', models.BooleanField(verbose_name='Do you and your mentor(s) meet over phone or video chat?')),
                ('intern_missed_meetings', models.BooleanField(verbose_name='Have you recently missed more than 2 meetings?')),
                ('talk_about_project_progress', models.BooleanField(verbose_name='Do you and your mentor(s) talk about project progress at least 3 days a week?')),
                ('reviewed_original_timeline', models.BooleanField(verbose_name='Have you and your mentor(s) reviewed the original project timeline?')),
                ('contribution_drafts', models.BooleanField(verbose_name='Do you share work-in-progress or draft contributions with your mentor(s)?')),
                ('contribution_review', models.BooleanField(verbose_name='Do your mentor(s) review your contributions within 1 to 3 days?')),
                ('contribution_revised', models.BooleanField(verbose_name='Do you revise your contribution(s) based on mentor feedback?')),
                ('mentor_shares_positive_feedback', models.BooleanField(verbose_name='Do your mentor(s) give you positive feedback and praise?')),
                ('mentor_promoting_work_to_community', models.BooleanField(verbose_name='Do your mentor(s) promote your contributions within your open source community?')),
                ('mentor_promoting_work_on_social_media', models.BooleanField(verbose_name='Do your mentor(s) promote your contributions on social media?')),
                ('intern_blogging', models.BooleanField(verbose_name='Have you been creating blog posts?')),
                ('mentor_discussing_blog', models.BooleanField(verbose_name='Do your mentor(s) discuss your blog posts with you?')),
                ('mentor_promoting_blog_to_community', models.BooleanField(verbose_name='Do your mentor(s) promote your blog posts to your open source community?')),
                ('mentor_promoting_blog_on_social_media', models.BooleanField(verbose_name='Do your mentor(s) promote your blog posts on social media?')),
                ('mentor_introduced_intern_to_community', models.BooleanField(verbose_name='Did your mentor(s) introduce you to your open source community?')),
                ('intern_asks_questions_of_community_members', models.BooleanField(verbose_name='Do you seek help from open source community members who are not your mentors?')),
                ('intern_talks_to_community_members', models.BooleanField(verbose_name='Do you have casual conversations with open source community members who are not your mentors?')),
                ('progress_report', models.TextField(verbose_name='Please provide a paragraph describing your communication frequency with your mentor(s), your progress on your project, and your interactions with your open source community. This will only be shown to Outreachy organizers and the Software Freedom Conservancy accounting staff.')),
                ('intern_selection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.internselection')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
