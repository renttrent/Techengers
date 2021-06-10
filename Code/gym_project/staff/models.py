from django.db import models


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    unit_price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'Item {self.name}'

    def getValue(self):
        return self.unit_price * self.quantity
