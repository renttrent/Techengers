# Generated by Django 3.2 on 2021-06-07 19:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('desc', models.TextField(blank=True)),
                ('thumbnail', models.ImageField(default='diets/default.jpg', upload_to='media/diets/')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 7, 21, 37, 3, 751791))),
                ('desc', models.TextField(blank=True)),
                ('thumbnail', models.ImageField(default='events/default.jpg', upload_to='media/events/')),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60)),
                ('desc', models.TextField(blank=True)),
                ('thumbnail', models.ImageField(default='routines/default.jpg', upload_to='media/routines/')),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60)),
                ('reps', models.IntegerField(blank=True, default=3)),
                ('desc', models.TextField(blank=True)),
                ('link', models.CharField(blank=True, max_length=300)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('routine', models.ManyToManyField(to='dashboards.Routine')),
            ],
        ),
    ]
