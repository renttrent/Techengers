from staff.notes import getNotes
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from dashboards.models import *
from django.contrib.admin.views.decorators import staff_member_required
from .navigation import *
from .models import *
from django.shortcuts import get_object_or_404


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
               'allevents': allevents, 'nrevents': len(allevents), 'notes': getNotes()}

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
    context['notes'] = getNotes()
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

    if request.POST:
        eid = request.POST['delete']
        if eid and Exercise.objects.get(id=eid):
            einstance = Exercise.objects.get(id=eid)
            einstance.delete()

    exercises = Exercise.objects.all()
    context = {'options': navigation, 'exercises': exercises}
    context['notes'] = getNotes()
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

    context = {'options': navigation}
    context['notes'] = getNotes()

    if request.POST:
        title = request.POST['title']
        reps = request.POST['reps']
        desc = request.POST['desc']
        link = request.POST['link']

        if title and reps and desc and link:
            ex = Exercise(title=title, reps=reps, desc=desc, link=link)
            ex.save()
            ex.selected_by.add(request.user)
            ex.save()
            return redirect('staff-manage-exercises')
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['repsValid'] = 'is-valid' if reps else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['linkValid'] = 'is-valid' if link else 'is-invalid'
            return render(request, 'staff/trainer/events/add_exercise.html', context)

    return render(request, 'staff/trainer/events/add_exercise.html', context)


@login_required(login_url='login')
@staff_member_required
def edit_exercise(request, eid):
    navigation = None
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_EXERCISES_NAV
        else:
            return redirect('staff')

    exercise = Exercise.objects.get(id=eid)
    context = {'options': navigation,
               'exercise': exercise}
    context['notes'] = getNotes()

    if request.POST:
        title = request.POST['title']
        reps = request.POST['reps']
        desc = request.POST['desc']
        link = request.POST['link']

        if title and reps and desc and link:
            ex = Exercise(title=title, reps=reps, desc=desc, link=link)
            ex.save()
            ex.selected_by.add(request.user)
            ex.save()
            return redirect('staff-manage-exercises')
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['repsValid'] = 'is-valid' if reps else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['linkValid'] = 'is-valid' if link else 'is-invalid'
            return render(request, 'staff/trainer/events/add_exercise.html', context)

    return render(request, 'staff/trainer/events/edit_exercise.html', context)


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
    context['notes'] = getNotes()

    if request.POST:
        delete = request.POST['delete']

        if delete and Routine.objects.get(id=int(delete)):
            d = Routine.objects.get(id=int(delete))
            d.delete()
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

    context = {'options': navigation, 'exercises': Exercise.objects.all()}
    context['days'] = ['Monday', 'Tuesday', 'Wednesday',
                       'Thursday', 'Friday', 'Saturday', 'Sunday']
    context['notes'] = getNotes()

    if request.POST:
        title = request.POST['title']
        desc = request.POST['desc']
        thumbnail = request.POST['thumbnail']
        days = request.POST.getlist('days')
        exercises_list = request.POST.getlist('exercises')

        if title and desc and days and exercises_list:
            if thumbnail:
                rt = Routine.objects.create(title=title, desc=desc,
                                            thumbnail=f'routines/{thumbnail}', owner=request.user)
            else:
                rt = Routine.objects.create(
                    title=title, desc=desc, owner=request.user)
            save_days = []
            for day in days:
                save_days.append(day)
            rt.days = ' '.join(save_days)
            rt.selected_by.add(request.user)

            for ex in exercises_list:
                exinstance = Exercise.objects.get(id=int(ex))
                rt.exercises.add(Exercise.objects.get(id=int(ex)))
                if request.user not in exinstance.selected_by.all():
                    exinstance.selected_by.add(request.user)
                exinstance.save()
            rt.save()
            return redirect('staff-manage-routines')
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['daysValid'] = 'is-valid' if days else 'is-invalid'
            context['exercisesValid'] = 'is-valid' if exercises_list else 'is-invalid'

            return render(request, 'staff/trainer/events/add_routine.html', context)

    return render(request, 'staff/trainer/events/add_routine.html', context)


@login_required(login_url='login')
@staff_member_required
def edit_routine(request, rid):

    navigation = None
    r = get_object_or_404(Routine, id=rid)
    if request.user.groups.first():
        role = request.user.groups.first().name
        if role == 'trainer':
            navigation = TRAINER_ROUTINES_NAV
        else:
            return redirect('staff')

    context = {'options': navigation, 'exercises': Exercise.objects.all(
    ), 'routine': r}

    context['days'] = ['Monday', 'Tuesday', 'Wednesday',
                       'Thursday', 'Friday', 'Saturday', 'Sunday']

    context['notes'] = getNotes()

    if request.POST:
        r = Routine.objects.get(id=rid)
        title = request.POST['title']
        desc = request.POST['desc']
        thumbnail = request.POST['thumbnail']
        days = request.POST.getlist('days')
        exercises_list = request.POST.getlist('exercises')
        print(title, days)
        if title and desc and days and exercises_list:
            if thumbnail:
                r.update(thumbnail=thumbnail)
            else:
                r.update(title=title)
                r.update(desc=desc)
                save_days = []
                for day in days:
                    save_days.append(day)
                r.update(days=' '.join(save_days))

                for ex in exercises_list:
                    r.exercises.add(Exercise.objects.get(id=int(ex)))
            return redirect('staff-manage-routines')
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['daysValid'] = 'is-valid' if days else 'is-invalid'
            context['exercisesValid'] = 'is-valid' if exercises_list else 'is-invalid'

            return render(request, 'staff/trainer/events/edit_routine.html', context)

    return render(request, 'staff/trainer/events/edit_routine.html', context)


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
    context['notes'] = getNotes()
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
    context['notes'] = getNotes()
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
    context['notes'] = getNotes()

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
    context['notes'] = getNotes()

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
    context['notes'] = getNotes()

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
    context['notes'] = getNotes()

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
    context['notes'] = getNotes()

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
    context['notes'] = getNotes()

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
    context['notes'] = getNotes()

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
