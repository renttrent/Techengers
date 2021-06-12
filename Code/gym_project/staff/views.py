from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from dashboards.models import *
from django.contrib.admin.views.decorators import staff_member_required
from .navigation import *
from .models import *
from datetime import datetime


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

    allusers = User.objects.all()
    allexercises = Exercise.objects.all()
    allroutines = Routine.objects.all()
    alldiets = DietPlan.objects.all()
    allevents = Event.objects.all()

    context = {'options': navigation,
               'allusers': allusers, 'nrusers': len(allusers), 'allexercises': allexercises, 'nrexercises': len(allexercises),
               'allroutines': allroutines, 'nrroutines': len(allroutines), 'alldiets': alldiets, 'nrdiets': len(alldiets),
               'allevents': allevents, 'nrevents': len(allevents)}

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
def add_exercise(request):

    navigation = None
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_EXERCISES_NAV
        else:
            return redirect('staff')

    exercises = Exercise.objects.all()
    routines = Routine.objects.all()
    context = {'options': navigation,
               'exercises': exercises, 'routines': routines}

    if request.POST:
        title = request.POST['title']
        reps = request.POST['reps']
        desc = request.POST['desc']
        link = request.POST['link']
        routine = request.POST['routines']

        if title and reps and desc and link and routine:
            ex = Exercise(title=title, reps=reps, desc=desc, link=link)
            ex.save()
            ex.routine.add(Routine.objects.get(id=routine))
            ex.selected_by.add(request.user)
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['repsValid'] = 'is-valid' if reps else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['linkValid'] = 'is-valid' if link else 'is-invalid'
            context['routineValid'] = 'is-valid' if routine else 'is-invalid'
            return render(request, 'staff/trainer/events/add_exercise.html', context)

    return render(request, 'staff/trainer/events/add_exercise.html', context)


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
def add_routine(request):

    navigation = None
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_ROUTINES_NAV
        else:
            return redirect('staff')

    routines = Routine.objects.all()
    context = {'options': navigation, 'routines': routines}
    context['days'] = ['Monday', 'Tuesday', 'Wednesday',
                       'Thursday', 'Friday', 'Saturday', 'Sunday']

    if request.POST:
        title = request.POST['title']
        desc = request.POST['desc']
        thumbnail = request.POST['thumbnail']
        days = request.POST.getlist('days')

        if title and desc and thumbnail and days:
            rt = Routine(title=title, desc=desc,
                         thumbnail=f'routines/{thumbnail}')
            save_days = []
            for day in days:
                save_days.append(day)
            rt.days = ' '.join(save_days)
            rt.save()
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['thumbnailValid'] = 'is-valid' if thumbnail else 'is-invalid'
            context['daysValid'] = 'is-valid' if days else 'is-invalid'

            return render(request, 'staff/trainer/events/add_routine.html', context)

    return render(request, 'staff/trainer/events/add_routine.html', context)


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
def add_staff(request):

    navigation = None

    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'economist':
            navigation = ECONOMIST_STAFF_NAV
        else:
            return redirect('staff')

    allusers = User.objects.all()
    context = {'options': navigation, 'allusers': allusers}

    # if request.POST:
    #     title = request.POST['title']
    #     desc = request.POST['desc']
    #     thumbnail = request.POST['thumbnail']
    #     days = request.POST.getlist('days')

    #     if title and desc and thumbnail and days:
    #         rt = Routine(title=title, desc=desc,
    #                      thumbnail=f'routines/{thumbnail}')
    #         save_days = []
    #         for day in days:
    #             save_days.append(day)
    #         rt.days = ' '.join(save_days)
    #         rt.save()
    #     else:
    #         context['error'] = 'Please fill in all fields!'
    #         context['titleValid'] = 'is-valid' if title else 'is-invalid'
    #         context['descValid'] = 'is-valid' if desc else 'is-invalid'
    #         context['thumbnailValid'] = 'is-valid' if thumbnail else 'is-invalid'
    #         context['daysValid'] = 'is-valid' if days else 'is-invalid'

    #         return render(request, 'staff/economist/events/add_staff.html', context)

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
def add_inventory(request):

    navigation = None

    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'manager':
            navigation = MANAGER_INVENTORY_NAV
        else:
            return redirect('staff')

    inventory = InventoryItem.objects.all()
    context = {'options': navigation, 'inventory': inventory}

    if request.POST:
        name = request.POST['name']
        desc = request.POST['desc']
        unit_price = request.POST['price']
        quantity = request.POST['quantity']

        if name and desc and unit_price and quantity:
            it = InventoryItem(name=name, desc=desc,
                               unit_price=unit_price, quantity=quantity)
            it.save()
        else:
            context['error'] = 'Please fill in all fields!'
            context['nameValid'] = 'is-valid' if name else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['priceValid'] = 'is-valid' if unit_price else 'is-invalid'
            context['quantityValid'] = 'is-valid' if quantity else 'is-invalid'

            return render(request, 'staff/manager/events/add_inventory.html', context)

    return render(request, f'staff/manager/events/add_inventory.html', context)


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
def add_event(request):

    navigation = None

    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'manager':
            navigation = MANAGER_EVENTS_NAV
        else:
            return redirect('staff')

    events = Event.objects.all()
    context = {'options': navigation, 'events': events}

    if request.POST:
        title = request.POST['title']
        desc = request.POST['desc']
        inputdate = request.POST['date']
        inputtime = request.POST['time']
        thumbnail = request.POST['thumbnail']

        if title and inputdate and desc and inputtime and thumbnail:
            year, month, day = tuple(map(int, inputdate.split("-")))
            hour, minute = tuple(map(int, inputtime.split(':')))
            dt = datetime(year, month, day, hour, minute)
            Event.objects.create(title=title, desc=desc,
                                 thumbnail=f'events/{thumbnail}', date=dt)
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['dateValid'] = 'is-valid' if inputdate else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['timeValid'] = 'is-valid' if inputtime else 'is-invalid'
            context['thumbnailValid'] = 'is-valid' if thumbnail else 'is-invalid'

            return render(request, 'staff/manager/events/add_event.html', context)

    return render(request, f'staff/manager/events/add_event.html', context)


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


@login_required(login_url='login')
@staff_member_required
def add_diet(request):

    navigation = None

    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'manager':
            navigation = MANAGER_DIETS_NAV
        else:
            return redirect('staff')

    diets = DietPlan.objects.all()
    context = {'options': navigation, 'diets': diets}

    if request.POST:
        title = request.POST['title']
        desc = request.POST['desc']
        thumbnail = request.POST['thumbnail']

        if title and desc and thumbnail:

            DietPlan.objects.create(
                title=title, desc=desc, thumbnail=f"diets/{thumbnail}")
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['thumbnailValid'] = 'is-valid' if thumbnail else 'is-invalid'

            return render(request, 'staff/manager/events/add_diet.html', context)

    return render(request, f'staff/manager/events/add_diet.html', context)
