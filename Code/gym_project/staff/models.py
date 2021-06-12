from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    unit_price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'Item {self.name}'

    def getValue(self):
        return self.unit_price * self.quantity


class AdminNotes(models.Model):
    todo = models.CharField(max_length=200)
    date = models.DateTimeField(
        default=datetime.now(), blank=True)

    def __str__(self):
        return f'Admin Note {self.id}'


class Workspace(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    salary = models.FloatField(default=0)
    working_days = models.CharField(max_length=200, default="")
    starts_work_at = models.DateTimeField(
        default=datetime.now(), blank=True)
    ends_work_at = models.DateTimeField(
        default=datetime.now(), blank=True)

    def __str__(self):
        return f"{self.user.username}'s Workspace"
