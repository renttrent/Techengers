# Generated by Django 3.2 on 2021-06-11 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0017_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 11, 9, 57, 49, 375715)),
        ),
    ]