import datetime
from django.db import models
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
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    desc = models.TextField(blank=True)
    thumbnail = models.ImageField(
        upload_to='events/', default='events/default.jpg')

    def __str__(self):
        return f"Event - {self.title}"

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)


class Routine(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=60, blank=True)
    desc = models.TextField(blank=True)
    thumbnail = models.ImageField(
        upload_to='routines/', default='routines/default.jpg')

    def __str__(self):
        return f"Routine - {self.title}"


class Exercise(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    routine = models.ManyToManyField(Routine)

    title = models.CharField(max_length=60, blank=True)
    reps = models.IntegerField(default=3, blank=True)
    desc = models.TextField(blank=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"Exercise - {self.title}"
