# Generated by Django 3.2.4 on 2021-06-12 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_auto_20210612_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminnotes',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 12, 17, 30, 30, 945696)),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='ends_work_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 12, 17, 30, 30, 945696)),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='starts_work_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 12, 17, 30, 30, 945696)),
        ),
    ]