from .models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Event)
admin.site.register(DietPlan)
admin.site.register(Exercise)
admin.site.register(Routine)
# admin.site.register(Day)

# if Day.objects.first():
#     DAYS_OPTIONS = ['Monday', 'Tuesday', 'Wednesday',
#                     'Thursday', 'Friday', 'Saturday', 'Sunday']
#     for day in DAYS_OPTIONS:
#         d = Day(day=day)
#         d.save()
