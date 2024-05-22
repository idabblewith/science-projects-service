# Generated by Django 5.0.6 on 2024-05-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminoptions', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminoptions',
            name='guide_about',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for about', null=True),
        ),
        migrations.AddField(
            model_name='adminoptions',
            name='guide_admin',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for admin', null=True),
        ),
        migrations.AddField(
            model_name='adminoptions',
            name='guide_documents',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for project documents', null=True),
        ),
        migrations.AddField(
            model_name='adminoptions',
            name='guide_login',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for login', null=True),
        ),
        migrations.AddField(
            model_name='adminoptions',
            name='guide_profile',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for profile', null=True),
        ),
        migrations.AddField(
            model_name='adminoptions',
            name='guide_project_creation',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for project creation', null=True),
        ),
        migrations.AddField(
            model_name='adminoptions',
            name='guide_project_team',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for project teams', null=True),
        ),
        migrations.AddField(
            model_name='adminoptions',
            name='guide_project_view',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for viewing projects', null=True),
        ),
        migrations.AddField(
            model_name='adminoptions',
            name='guide_report',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for annual report', null=True),
        ),
        migrations.AddField(
            model_name='adminoptions',
            name='guide_user_creation',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for user creation', null=True),
        ),
        migrations.AddField(
            model_name='adminoptions',
            name='guide_user_view',
            field=models.TextField(blank=True, help_text='Provide RTE data to be displayed on the guide for viewing users', null=True),
        ),
    ]
