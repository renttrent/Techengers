from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    height = models.FloatField()
    weight = models.FloatField()
    weight_goal = models.FloatField()
