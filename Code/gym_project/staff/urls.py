from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name="staff"),
    path('activity/', views.latest_activity, name="staff-latest-activity"),
    path('profile/', views.profile, name="staff-profile"),

    path('exercises/', views.manage_exercises, name="staff-manage-exercises"),
    path('exercises/add', views.add_exercise, name="staff-add-exercise"),
    path('exercises/edit/<int:eid>',
         views.edit_exercise, name="staff-edit-exercise"),


    path('routines/', views.manage_routines, name="staff-manage-routines"),
    path('routines/add', views.add_routine, name="staff-add-routine"),
    path('routines/edit/<int:rid>',
         views.edit_routine, name="staff-edit-routine"),

    path('workspace/', views.workspace, name="staff-workspace"),
    path('workspace/edit', views.edit_workspace, name="staff-edit-workspace"),

    path('manage-staff/', views.manage_staff, name="staff-manage-staff"),
    path('manage-staff/add', views.add_staff, name="staff-add-staff"),

    path('inventory/', views.manage_inventory,
         name="staff-manage-inventory"),
    path('inventory/add/', views.add_inventory,
         name="staff-add-inventory"),
    path('inventory/edit/<int:id>', views.edit_inventory,
         name="staff-edit-inventory"),

    path('diets/', views.manage_diets,
         name="staff-manage-diets"),
    path('diets/add', views.add_diet,
         name="staff-add-diet"),

    path('events/', views.manage_events,
         name="staff-manage-events"),
    path('events/add', views.add_event,
         name="staff-add-event"),

    path('view-inventory/', views.view_inventory,
         name="staff-view-inventory"),
]
