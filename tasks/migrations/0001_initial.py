# Generated by Django 5.0.2 on 2024-02-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=2000, null=True)),
                ('status', models.CharField(choices=[('todo', 'To Do'), ('inprogress', 'In Progress'), ('done', 'Done')], default='todo', max_length=20)),
                ('task_type', models.CharField(choices=[('personal', 'Personal'), ('assigned', 'Assigned')], max_length=20)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kind', models.CharField(choices=[('feedback', 'Feedback'), ('request', 'Feature Request')], default='feedback', max_length=20)),
                ('text', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('logged', 'Logged'), ('inprogress', 'In Progress'), ('fixed', 'Fixed')], default='new', max_length=20)),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'User Feedback',
            },
        ),
    ]
