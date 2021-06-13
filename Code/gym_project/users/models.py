from dashboards.models import DietPlan
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_photo = models.ImageField(
        upload_to='media/profiles/', default='profiles/default.jpg')

    height = models.FloatField(default=170.0)
    weight = models.FloatField(default=60.0)
    weight_goal = models.FloatField(default=70.0)

    GENDER_CHOICES = (('F', 'Female'), ('M', 'Male'), ('O', 'Other'))
    gender = models.CharField(
        max_length=9, choices=GENDER_CHOICES, default=GENDER_CHOICES[0])

    FREQUENCY = (
        ('3x', '3 Times a Week'),
        ('4x', '4 Times a Week'),
        ('5x', '5 Times a Week'),
        ('6x', '6 Times a Week'),
    )
    week_frequency = models.CharField(
        max_length=20, choices=FREQUENCY, default=FREQUENCY[0])

    profile_complete = models.BooleanField(default=False)

    selected_diets = models.ManyToManyField(DietPlan, blank=True)

    age = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
