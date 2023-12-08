# Generated by Django 5.0 on 2023-12-08 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Affiliation',
                'verbose_name_plural': 'Affiliations',
            },
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Agency',
                'verbose_name_plural': 'Agencies',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('old_id', models.IntegerField()),
                ('name', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='BusinessArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('slug', models.SlugField(help_text="A URL-sage acronym of the BA's name without whitespace")),
                ('published', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('cost_center', models.IntegerField(blank=True, null=True)),
                ('old_leader_id', models.IntegerField(blank=True, null=True)),
                ('old_finance_admin_id', models.IntegerField(blank=True, null=True)),
                ('old_data_custodian_id', models.IntegerField(blank=True, null=True)),
                ('old_id', models.IntegerField()),
                ('focus', models.CharField(blank=True, max_length=1250, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Business Area',
                'verbose_name_plural': 'Business Areas',
            },
        ),
        migrations.CreateModel(
            name='DepartmentalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=320)),
                ('old_id', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Departmental Service',
                'verbose_name_plural': 'Departmental Services',
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('old_id', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(help_text="A URL-sage acronym of the Division's name without whitespace")),
            ],
            options={
                'verbose_name': 'Department Division',
                'verbose_name_plural': 'Department Divisions',
            },
        ),
    ]
