# Generated by Django 3.2.4 on 2021-06-13 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0033_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 13, 18, 51, 37, 787107)),
        ),
    ]