# Generated by Django 3.2.4 on 2021-06-12 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0021_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 12, 16, 14, 41, 779565)),
        ),
    ]
