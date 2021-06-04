import datetime
from django.db import models
from django.utils import timezone


class DietPlan(models.Model):
    diet_name = models.CharField(max_length=30)
    diet_dscr = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diet Plan - {self.diet_name}"


class Event(models.Model):
    event_name = models.CharField(max_length=60)
    pub_date = models.DateTimeField('date published')
    event_dscr = models.TextField()

    def __str__(self):
        return f"Event - {self.event_name}"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=60)
    exercise_dscr = models.TextField()
    exercise_thumbnail = models.ImageField(upload_to="media")

    def __str__(self):
        return f"Exercise - {self.exercise_name}"


class Routine(models.Model):
    routine_name = models.CharField(max_length=60)
    routine_dscr = models.TextField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"Routine - {self.routine_name}"
