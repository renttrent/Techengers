from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_photo = models.ImageField(upload_to='profiles')

    height = models.FloatField()
    weight = models.FloatField()
    weight_goal = models.FloatField()

    GENDER_CHOICES = [('F', 'Female'), ('M', 'Male'), ('O', 'Other')]
    gender = models.CharField(
        max_length=9, choices=GENDER_CHOICES)

    FREQUENCY = [
        ('3x', '3 Times a Week'),
        ('4x', '4 Times a Week'),
        ('5x', '5 Times a Week'),
        ('6x', '6 Times a Week'),
    ]
    week_frequency = models.CharField(max_length=20, choices=FREQUENCY)

    profile_complete = False

    def __str__(self):
        return f"{self.user}'s Profile"
