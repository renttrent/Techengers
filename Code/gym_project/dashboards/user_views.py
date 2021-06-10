from dashboards.navigation import DIETS_NAV, EXERCISES_NAV, ROUTINES_NAV, SCHEDULE_NAV, TRAINERS_NAV
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Event, Exercise, Routine
from datetime import datetime


@login_required(login_url='login')
def home(request):
    return redirect('userdashboard-schedule')


@login_required(login_url='login')
def schedule(request):

    events = Event.objects.all()[:4]
    week_num = datetime.today().date().weekday()

    routines = Routine.objects.filter(
        selected_by__username=request.user.username)
    today = None
    if routines:
        today = routines[0].DAYS_OPTIONS[week_num][1]
    context = {'options': SCHEDULE_NAV,
               'events': events, 'schedule': routines, 'today': today}
    return render(request, 'dashboards/user/schedule.html', context)


@login_required(login_url='login')
def exercises(request):

    events = Event.objects.all()[:4]
    exercises = Exercise.objects.all()
    context = {'options': EXERCISES_NAV,
               'events': events, 'exercises': exercises}
    return render(request, 'dashboards/user/exercises.html', context)


@login_required(login_url='login')
def routines(request):

    events = Event.objects.all()[:4]
    routines = Routine.objects.all()
    context = {'options': ROUTINES_NAV, 'events': events, 'routines': routines}
    return render(request, 'dashboards/user/routines.html', context)


@login_required(login_url='login')
def diets(request):

    events = Event.objects.all()[:4]
    context = {'options': DIETS_NAV, 'events': events}
    return render(request, 'dashboards/user/diets.html', context)


@login_required(login_url='login')
def trainers(request):

    events = Event.objects.all()[:4]
    context = {'options': TRAINERS_NAV, 'events': events}
    return render(request, 'dashboards/user/trainers.html', context)
