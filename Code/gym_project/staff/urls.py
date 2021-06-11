from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name="staff"),
    path('activity/', views.latest_activity, name="staff-latest-activity"),
    path('exercises/', views.manage_exercises, name="staff-manage-exercises"),
    path('routines/', views.manage_routines, name="staff-manage-routines"),
    path('workspace/', views.workspace, name="staff-workspace"),
    path('manage-staff/', views.manage_staff, name="staff-manage-staff"),
    path('inventory/', views.manage_inventory,
         name="staff-manage-inventory"),
    path('diets/', views.manage_diets,
         name="staff-manage-diets"),
    path('events/', views.manage_events,
         name="staff-manage-events"),
    path('view-inventory/', views.view_inventory,
         name="staff-view-inventory"),
]
