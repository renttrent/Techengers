from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import user_views

urlpatterns = [
    path('', user_views.home, name="userdashboard"),

    path('profile/', user_views.profile, name='profile'),
    path('profile/edit/', user_views.edit_profile, name='edit-profile'),
    path('profile/changepassword/',
         user_views.change_password, name='change-password'),

    path('schedule/', user_views.schedule, name='userdashboard-schedule'),

    path('exercises/', user_views.exercises,
         name='userdashboard-exercises'),
    path('exercise/<int:eid>', user_views.exercise_details,
         name='userdashboard-exercise-details'),
    path('exercise/create', user_views.create_exercise, name='create-exercise'),
    path('exercise/<int:eid>/edit', user_views.edit_exercise, name='edit-exercise'),

    path('routines/', user_views.routines,
         name='userdashboard-routines'),
    path('routine/<int:rid>', user_views.routine_details,
         name='userdashboard-routine-details'),
    path('routine/create', user_views.create_routine, name='create-routine'),
    path('routine/<int:rid>/edit', user_views.edit_routine, name='edit-routine'),

    path('diets/', user_views.diets, name='userdashboard-diets'),

    path('trainers/', user_views.trainers,
         name='userdashboard-trainers'),
    path('trainer/<int:tid>', user_views.trainer_details,
         name='userdashboard-trainer-details'),

]
