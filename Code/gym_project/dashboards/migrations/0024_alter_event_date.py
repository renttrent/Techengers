# Generated by Django 3.2.4 on 2021-06-12 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0023_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 6, 12, 17, 30, 30, 938695)),
        ),
    ]
