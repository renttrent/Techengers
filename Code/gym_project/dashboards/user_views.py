from dashboards.navigation import DIETS_NAV, EXERCISES_NAV, ROUTINES_NAV, SCHEDULE_NAV, TRAINERS_NAV
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Event, Exercise, Routine
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


@login_required(login_url='login')
def home(request):
    if request.user.is_superuser:
        return redirect('/admin')
    if request.user.is_staff:
        return redirect('staff')
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
def exercise_details(request, eid):
    events = Event.objects.all()[:4]
    e = get_object_or_404(Exercise, id=eid)
    if e:
        context = {'options': EXERCISES_NAV,
                   'events': events, 'exercise': e}
        return render(request, 'dashboards/user/show_exercise.html', context)


@login_required(login_url='login')
def routines(request):

    events = Event.objects.all()[:4]
    routines = Routine.objects.all()
    context = {'options': ROUTINES_NAV, 'events': events, 'routines': routines}
    return render(request, 'dashboards/user/routines.html', context)


@login_required(login_url='login')
def routine_details(request, rid):

    events = Event.objects.all()[:4]
    r = get_object_or_404(Routine, id=rid)
    if r:

        context = {'options': ROUTINES_NAV, 'events': events, 'routine': r}
        return render(request, 'dashboards/user/show_routine.html', context)


@login_required(login_url='login')
def diets(request):

    events = Event.objects.all()[:4]
    context = {'options': DIETS_NAV, 'events': events}
    return render(request, 'dashboards/user/diets.html', context)


@login_required(login_url='login')
def trainers(request):

    events = Event.objects.all()[:4]
    trainers = User.objects.all().filter(groups__name='trainer')
    context = {'options': TRAINERS_NAV, 'events': events, 'trainers': trainers}
    return render(request, 'dashboards/user/trainers.html', context)


@login_required(login_url='login')
def trainer_details(request, tid):

    events = Event.objects.all()[:4]
    t = get_object_or_404(User, id=tid)
    if t:
        if t.is_staff and t.groups.first().name == 'trainer':
            context = {'options': TRAINERS_NAV, 'events': events, 'trainer': t}
            return render(request, 'dashboards/user/show_trainer.html', context)
        else:
            return redirect('userdashboard-trainers')


@login_required(login_url='login')
def profile(request):

    events = Event.objects.all()[:4]

    context = {'options': SCHEDULE_NAV,
               'events': events}
    return render(request, 'dashboards/user/profile.html', context)


@login_required(login_url='login')
def create_exercise(request):
    events = Event.objects.all()[:4]
    routines = Routine.objects.all()
    context = {'options': EXERCISES_NAV,
               'events': events, 'routines': routines}

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
            return render(request, 'dashboards/user/events/create_exercise.html', context)

    return render(request, 'dashboards/user/events/create_exercise.html', context)


@login_required(login_url='login')
def create_routine(request):
    events = Event.objects.all()[:4]
    context = {'options': ROUTINES_NAV,
               'events': events}
    context['days'] = ['Monday', 'Tuesday', 'Wednesday',
                       'Thursday', 'Friday', 'Saturday', 'Sunday']
    if request.POST:
        title = request.POST['title']
        desc = request.POST['desc']
        thumbnail = request.POST['thumbnail']
        days = request.POST.getlist('days')

        if title and desc and thumbnail and days:
            rt = Routine(title=title, desc=desc, thumbnail=thumbnail)
            save_days = []
            for day in days:
                save_days.append((day, day))
            rt.days = save_days
            rt.save()
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['thumbnailValid'] = 'is-valid' if thumbnail else 'is-invalid'
            context['daysValid'] = 'is-valid' if days else 'is-invalid'

            return render(request, 'dashboards/user/events/create_routine.html', context)

    return render(request, 'dashboards/user/events/create_routine.html', context)
