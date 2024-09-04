# Generated by Django 5.0.6 on 2024-08-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0003_marker_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marker',
            name='is_permanent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='marker',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
