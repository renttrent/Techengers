# Generated by Django 3.2.4 on 2021-06-12 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0022_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2021, 6, 12)),
        ),
    ]
