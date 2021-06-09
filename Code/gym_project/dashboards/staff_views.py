from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Event, Exercise, Routine


@login_required(login_url='login')
def schedule(request):
    navigation = {
        'schedule': {
            'name': 'Schedule',
            'isActive': True,
            'url': 'schedule'
        },
        'exercises': {
            'name': 'Exercises',
            'isActive': False,
            'url': 'exercises'
        },
        'routines': {
            'name': 'Routines',
            'isActive': False,
            'url': 'routines'
        },
        'diets': {
            'name': 'Selected Diets',
            'isActive': False,
            'url': 'diets'
        },
        'trainers': {
            'name': 'Trainers',
            'isActive': False,
            'url': 'trainers'
        },
    }
    events = Event.objects.all()[:4]

    schedule = Routine.objects.filter(owner=request.user)

    context = {'options': navigation, 'events': events, 'schedule': schedule}
    return render(request, 'dashboards/user/schedule.html', context)


@login_required(login_url='login')
def exercises(request):
    navigation = {
        'schedule': {
            'name': 'Schedule',
            'isActive': False,
            'url': 'schedule'
        },
        'exercises': {
            'name': 'Exercises',
            'isActive': True,
            'url': 'exercises'
        },
        'routines': {
            'name': 'Routines',
            'isActive': False,
            'url': 'routines'
        },
        'diets': {
            'name': 'Selected Diets',
            'isActive': False,
            'url': 'diets'
        },
        'trainers': {
            'name': 'Trainers',
            'isActive': False,
            'url': 'trainers'
        },
    }
    events = Event.objects.all()[:4]
    exercises = Exercise.objects.all()
    context = {'options': navigation, 'events': events, 'exercises': exercises}
    return render(request, 'dashboards/user/exercises.html', context)


@login_required(login_url='login')
def routines(request):
    navigation = {
        'schedule': {
            'name': 'Schedule',
            'isActive': False,
            'url': 'schedule'
        },
        'exercises': {
            'name': 'Exercises',
            'isActive': False,
            'url': 'exercises'
        },
        'routines': {
            'name': 'Routines',
            'isActive': True,
            'url': 'routines'
        },
        'diets': {
            'name': 'Selected Diets',
            'isActive': False,
            'url': 'diets'
        },
        'trainers': {
            'name': 'Trainers',
            'isActive': False,
            'url': 'trainers'
        },
    }
    events = Event.objects.all()[:4]
    routines = Routine.objects.all()
    context = {'options': navigation, 'events': events, 'routines': routines}
    return render(request, 'dashboards/user/routines.html', context)


@login_required(login_url='login')
def diets(request):
    navigation = {
        'schedule': {
            'name': 'Schedule',
            'isActive': False,
            'url': 'schedule'
        },
        'exercises': {
            'name': 'Exercises',
            'isActive': False,
            'url': 'exercises'
        },
        'routines': {
            'name': 'Routines',
            'isActive': False,
            'url': 'routines'
        },
        'diets': {
            'name': 'Selected Diets',
            'isActive': True,
            'url': 'diets'
        },
        'trainers': {
            'name': 'Trainers',
            'isActive': False,
            'url': 'trainers'
        },
    }
    events = Event.objects.all()[:4]
    context = {'options': navigation, 'events': events}
    return render(request, 'dashboards/user/diets.html', context)


@login_required(login_url='login')
def trainers(request):
    navigation = {
        'schedule': {
            'name': 'Schedule',
            'isActive': False,
            'url': 'schedule'
        },
        'exercises': {
            'name': 'Exercises',
            'isActive': False,
            'url': 'exercises',
        },
        'routines': {
            'name': 'Routines',
            'isActive': False,
            'url': 'routines'
        },
        'diets': {
            'name': 'Selected Diets',
            'isActive': False,
            'url': 'diets'
        },
        'trainers': {
            'name': 'Trainers',
            'isActive': True,
            'url': 'trainers'
        },
    }
    events = Event.objects.all()[:4]
    context = {'options': navigation, 'events': events}
    return render(request, 'dashboards/user/trainers.html', context)
