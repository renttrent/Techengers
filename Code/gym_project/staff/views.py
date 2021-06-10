from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from dashboards.models import Event, Exercise, Routine
from django.contrib.admin.views.decorators import staff_member_required
from .navigation import *


@login_required(login_url='login')
@staff_member_required
def home(request):
    return redirect('staff-latest-activity')


@login_required(login_url='login')
@staff_member_required
def latest_activity(request):

    navigation = None
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_ACTIVITY_NAV
        elif role == 'manager':
            pass
        elif role == 'economist':
            pass

    context = {'options': navigation}
    return render(request, 'staff/shared/activity.html', context)


@login_required(login_url='login')
@staff_member_required
def manage_exercises(request):

    navigation = None
    html = 'base'
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_EXERCISES_NAV
            html = 'trainer/manage_exercises'
        elif role == 'manager':
            html = 'manager/activity'
        elif role == 'economist':
            html = 'economist/activity'

    context = {'options': navigation}
    return render(request, f'staff/{html}.html', context)


@login_required(login_url='login')
@staff_member_required
def manage_routines(request):

    navigation = None
    html = 'base'
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_ROUTINES_NAV
            html = 'trainer/manage_routines'
        elif role == 'manager':
            html = 'manager/activity'
        elif role == 'economist':
            html = 'economist/activity'

    context = {'options': navigation}
    return render(request, f'staff/{html}.html', context)


@login_required(login_url='login')
@staff_member_required
def workspace(request):

    navigation = None
    html = 'base'
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_WORK_NAV
            html = 'trainer/workspace'
        elif role == 'manager':
            html = 'manager/workspace'
        elif role == 'economist':
            html = 'economist/workspace'

    context = {'options': navigation}
    return render(request, f'staff/{html}.html', context)
