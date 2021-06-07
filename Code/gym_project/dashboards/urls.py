from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name="userdashboard"),
    path('schedule/', views.schedule, name='userdashboard-schedule'),
    path('exercises/', views.exercises, name='userdashboard-exercises'),
    path('routines/', views.routines, name='userdashboard-routines'),
    path('diets/', views.diets, name='userdashboard-diets'),
    path('trainers/', views.trainers, name='userdashboard-trainers'),
]
