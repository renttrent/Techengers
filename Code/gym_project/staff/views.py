from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from dashboards.models import *
from django.contrib.admin.views.decorators import staff_member_required
from .navigation import *
from .models import *


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
            navigation = MANAGER_ACTIVITY_NAV
        elif role == 'economist':
            navigation = ECONOMIST_ACTIVITY_NAV

    context = {'options': navigation}
    return render(request, 'staff/shared/activity.html', context)


@login_required(login_url='login')
@staff_member_required
def workspace(request):

    navigation = None
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_WORK_NAV
        elif role == 'manager':
            navigation = MANAGER_WORK_NAV
        elif role == 'economist':
            navigation = ECONOMIST_WORK_NAV

    context = {'options': navigation}
    return render(request, 'staff/shared/workspace.html', context)


@login_required(login_url='login')
@staff_member_required
def manage_exercises(request):

    navigation = None
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_EXERCISES_NAV
        else:
            return redirect('staff')

    exercises = Exercise.objects.all()
    context = {'options': navigation, 'exercises': exercises}
    return render(request, f'staff/trainer/exercises.html', context)


@login_required(login_url='login')
@staff_member_required
def manage_routines(request):

    navigation = None
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_ROUTINES_NAV
        else:
            return redirect('staff')

    routines = Routine.objects.all()
    context = {'options': navigation, 'routines': routines}
    return render(request, f'staff/trainer/routines.html', context)


@login_required(login_url='login')
@staff_member_required
def manage_staff(request):

    navigation = None

    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'economist':
            navigation = ECONOMIST_STAFF_NAV
        else:
            return redirect('staff')

    allusers = User.objects.all()
    context = {'options': navigation, 'allusers': allusers}
    return render(request, f'staff/economist/manage_staff.html', context)


@login_required(login_url='login')
@staff_member_required
def view_inventory(request):

    navigation = None

    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'economist':
            navigation = ECONOMIST_INVENTORY_NAV
        else:
            return redirect('staff')

    inventory = InventoryItem.objects.all()
    context = {'options': navigation, 'inventory': inventory}
    return render(request, f'staff/economist/view_inventory.html', context)


@login_required(login_url='login')
@staff_member_required
def manage_inventory(request):

    navigation = None

    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'manager':
            navigation = MANAGER_INVENTORY_NAV
        else:
            return redirect('staff')

    inventory = InventoryItem.objects.all()
    context = {'options': navigation, 'inventory': inventory}
    return render(request, f'staff/manager/manage_inventory.html', context)


@login_required(login_url='login')
@staff_member_required
def manage_events(request):

    navigation = None

    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'manager':
            navigation = MANAGER_EVENTS_NAV
        else:
            return redirect('staff')

    events = Event.objects.all()
    context = {'options': navigation, 'events': events}
    return render(request, f'staff/manager/manage_events.html', context)


@login_required(login_url='login')
@staff_member_required
def manage_diets(request):

    navigation = None

    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'manager':
            navigation = MANAGER_DIETS_NAV
        else:
            return redirect('staff')

    diets = DietPlan.objects.all()
    context = {'options': navigation, 'diets': diets}
    return render(request, f'staff/manager/manage_diets.html', context)
