from django.db import models
from django.utils import timezone


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
    date = models.DateField(blank=True)

    def __str__(self):
        return f'Admin Note {self.id}'
