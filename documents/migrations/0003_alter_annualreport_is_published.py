# Generated by Django 5.0.6 on 2024-06-07 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualreport',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
