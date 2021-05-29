# Generated by Django 3.2 on 2021-05-29 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet_name', models.CharField(max_length=30)),
                ('diet_dscr', models.TextField()),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=60)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('event_dscr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=60)),
                ('exercise_dscr', models.TextField()),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routime_name', models.CharField(max_length=60)),
                ('routime_dscr', models.TextField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboards.exercise')),
            ],
        ),
    ]