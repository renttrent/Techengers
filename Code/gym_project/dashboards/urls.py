from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import user_views

urlpatterns = [
    path('', user_views.home, name="userdashboard"),
    path('schedule/', user_views.schedule, name='userdashboard-schedule'),
    path('exercises/', user_views.exercises, name='userdashboard-exercises'),
    path('routines/', user_views.routines, name='userdashboard-routines'),
    path('diets/', user_views.diets, name='userdashboard-diets'),
    path('trainers/', user_views.trainers, name='userdashboard-trainers'),
]
