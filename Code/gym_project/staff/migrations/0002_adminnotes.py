# Generated by Django 3.2 on 2021-06-11 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.datetime(2021, 6, 11, 9, 56, 35, 161706))),
            ],
        ),
    ]