from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name="staff"),
    path('activity/', views.latest_activity, name="staff-latest-activity"),
]
