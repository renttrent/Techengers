from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User


class DietPlan(models.Model):
    title = models.CharField(max_length=30, blank=True)
    desc = models.TextField(blank=True)
    thumbnail = models.ImageField(
        upload_to='diets/', default='diets/default.jpg')

    def __str__(self):
        return f"Diet Plan - {self.title}"


class Event(models.Model):
    title = models.CharField(max_length=60, blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    desc = models.TextField(blank=True)
    thumbnail = models.ImageField(
        upload_to='events/', default='events/default.jpg')

    def __str__(self):
        return f"Event - {self.title}"

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)


class Exercise(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE,
                              related_name='%(class)s_username', null=True)
    selected_by = models.ManyToManyField(User)
    title = models.CharField(max_length=60, blank=True)
    reps = models.IntegerField(default=3, blank=True)
    desc = models.TextField(blank=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"Exercise - {self.title}"


class Routine(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE,
                              related_name='%(class)s_username', null=True)
    title = models.CharField(max_length=60, blank=True)
    selected_by = models.ManyToManyField(User)
    desc = models.TextField(blank=True)
    thumbnail = models.ImageField(
        upload_to='routines/', default='routines/default.jpg')
    exercises = models.ManyToManyField(Exercise)
    days = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f"Routine - {self.title}"
