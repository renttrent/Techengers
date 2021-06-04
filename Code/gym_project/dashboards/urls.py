from django.urls import path

from . import views

urlpatterns = [
    path('userdashboard/', views.home, name="userdashboard"),
]
