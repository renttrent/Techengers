from dashboards.navigation import DIETS_NAV, EXERCISES_NAV, ROUTINES_NAV, SCHEDULE_NAV, TRAINERS_NAV
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import DietPlan, Event, Exercise, Routine
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
    WEEK_DAYS = ["Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday"]
    week_num = datetime.today().date().weekday()
    WEEK_DAYS = WEEK_DAYS[week_num:] + WEEK_DAYS[:week_num]
    DISPLAY_WEEK_DAYS = ['Today'] + WEEK_DAYS[1:]

    routines = list(Routine.objects.filter(
        selected_by__username=request.user.username))

    context = {'options': SCHEDULE_NAV,
               'events': events, 'routines': routines}

    day_dict = None
    compare = Routine()
    if routines:
        day_dict = {}
        for day in WEEK_DAYS:
            daily_routines = []
            for r in routines:
                if day in r.days:
                    daily_routines.append(r)
            day_dict[day] = daily_routines
    if day_dict:
        context['day_dict'] = zip(day_dict.items(), DISPLAY_WEEK_DAYS)
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
        if "watch?v=" in e.link:
            embeded = e.link.replace("watch?v=", "embed/")
        else:
            embeded = 'https://www.youtube.com/embed/' + e.link[17:]

        context = {'options': EXERCISES_NAV,
                   'events': events, 'exercise': e, 'embeded': embeded}

        if request.POST:
            e.delete()
            return redirect('userdashboard-exercises')

        return render(request, 'dashboards/user/show_exercise.html', context)


@login_required(login_url='login')
def routines(request):

    events = Event.objects.all()[:4]
    routines = Routine.objects.all()
    context = {'options': ROUTINES_NAV, 'events': events, 'routines': routines}

    if request.POST:
        deselect = request.POST['deselect']
        select = request.POST['select']

        if deselect and select:

            if int(deselect) > 0:
                routine = Routine.objects.get(id=deselect)
                routine.selected_by.remove(request.user)
            if int(select) > 0:
                routine = Routine.objects.get(id=select)
                routine.selected_by.add(request.user)
            return render(request, 'dashboards/user/routines.html', context)

    return render(request, 'dashboards/user/routines.html', context)


@login_required(login_url='login')
def routine_details(request, rid):

    events = Event.objects.all()[:4]
    r = get_object_or_404(Routine, id=rid)
    if r:
        ex = r.exercises.all()
        context = {'options': ROUTINES_NAV,
                   'events': events, 'routine': r, 'exercises': ex}

        if request.POST:
            r.delete()
            return redirect('userdashboard-routines')

        return render(request, 'dashboards/user/show_routine.html', context)


@login_required(login_url='login')
def diets(request):

    events = Event.objects.all()[:4]
    diets = DietPlan.objects.all()

    context = {'options': DIETS_NAV, 'events': events, 'diets': diets}

    if request.POST:
        select = request.POST['select']
        remove = request.POST['remove']
        if select and remove:
            if int(select) > 0:
                request.user.profile.selected_diets.add(
                    DietPlan.objects.get(id=select))
            if int(remove) > 0:
                request.user.profile.selected_diets.remove(
                    DietPlan.objects.get(id=remove))

        return render(request, 'dashboards/user/diets.html', context)

    return render(request, 'dashboards/user/diets.html', context)


@login_required(login_url='login')
def trainers(request):

    events = Event.objects.all()[:4]
    routines = Routine.objects.all()
    routines_owned = []
    trainers = User.objects.all().filter(groups__name='trainer')
    for trainer in trainers:
        routines_owned.append(
            sum([1 for ru in routines if ru.owner == trainer]))

    context = {'options': TRAINERS_NAV, 'events': events,
               'trainers_info': zip(trainers, routines_owned)}
    return render(request, 'dashboards/user/trainers.html', context)


@login_required(login_url='login')
def trainer_details(request, tid):

    events = Event.objects.all()[:4]
    routines = Routine.objects.all()
    t = get_object_or_404(User, id=tid)
    if t:
        routines = [ru for ru in routines if ru.owner == t]
        routines_owned = len(routines)

        if t.is_staff and t.groups.first().name == 'trainer':
            context = {'options': TRAINERS_NAV, 'events': events,
                       'trainer': t, 'routines_owned': routines_owned, 'routines': routines}

            worktime = t.workspace.starts_work_at.strftime(
                '%H:%M'), t.workspace.starts_work_at.strftime('%H:%M')
            context['working_days'] = [
                f'{day} - {worktime[0]} until {worktime[1]}' for day in t.workspace.working_days.split(' ')]

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
def edit_profile(request):

    events = Event.objects.all()[:4]

    context = {'options': SCHEDULE_NAV,
               'events': events}

    if request.POST:
        username = request.POST['username']
        age = request.POST['age']
        weight = request.POST['weight']
        height = request.POST['height']
        weight_goal = request.POST['weight_goal']
        week_frequency = request.POST['week_frequency']

        if username and age and weight and height and weight_goal and week_frequency:
            userinstance = request.user
            userinstance.username = username
            userinstance.profile.age = age
            userinstance.profile.weight = weight
            userinstance.profile.height = height
            userinstance.profile.weight_goal = weight_goal
            userinstance.profile.week_frequency = week_frequency
            userinstance.save()
            return redirect('profile')
        else:
            context['error'] = 'Please fill in all fields!'
            context['usernameValid'] = 'is-valid' if username else 'is-invalid'
            context['ageValid'] = 'is-valid' if age else 'is-invalid'
            context['weightValid'] = 'is-valid' if weight else 'is-invalid'
            context['heightValid'] = 'is-valid' if height else 'is-invalid'
            context['weightGoalValid'] = 'is-valid' if weight_goal else 'is-invalid'
            context['weekFrequencyValid'] = 'is-valid' if week_frequency else 'is-invalid'
            return render(request, 'dashboards/user/events/edit_profile.html', context)

    return render(request, 'dashboards/user/events/edit_profile.html', context)


@login_required(login_url='login')
def change_password(request):

    events = Event.objects.all()[:4]

    context = {'options': SCHEDULE_NAV,
               'events': events}

    if request.POST:
        userinstance = request.user
        old = request.POST['old']
        old2 = request.POST['old2']
        new = request.POST['new']
        new2 = request.POST['new2']

        if old != old2:
            context['error'] = 'Your old passwords do not match!'
            context['oldValid'] = 'is-valid' if userinstance.check_password(
                old) else 'is-invalid'
            context['old2Valid'] = 'is-valid' if userinstance.check_password(
                old2) else 'is-invalid'
            return render(request, 'dashboards/user/events/change_password.html', context)

        if userinstance.check_password(old) and userinstance.check_password(old2):
            if new == new2:
                userinstance.set_password(new)
                userinstance.save()
                return redirect('profile')
            else:
                context['error'] = 'Your new passwords do not match!'
                context['newValid'] = 'is-valid' if userinstance.check_password(
                    new) else 'is-invalid'
                context['new2Valid'] = 'is-valid' if userinstance.check_password(
                    new2) else 'is-invalid'
                return render(request, 'dashboards/user/events/change_password.html', context)

        else:
            context['error'] = 'Your old passwords are wrong!'
            context['oldValid'] = 'is-valid' if userinstance.check_password(
                old) else 'is-invalid'
            context['old2Valid'] = 'is-valid' if userinstance.check_password(
                old2) else 'is-invalid'
            return render(request, 'dashboards/user/events/change_password.html', context)
    return render(request, 'dashboards/user/events/change_password.html', context)


@login_required(login_url='login')
def create_exercise(request):
    events = Event.objects.all()[:4]
    context = {'options': EXERCISES_NAV,
               'events': events}

    if request.POST:
        title = request.POST['title']
        reps = request.POST['reps']
        desc = request.POST['desc']
        link = request.POST['link']

        if title and reps and desc and link:
            ex = Exercise(owner=request.user, title=title,
                          reps=reps, desc=desc, link=link)
            ex.save()
            ex.selected_by.add(request.user)
            ex.save()
            return redirect('userdashboard-exercises')
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['repsValid'] = 'is-valid' if reps else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['linkValid'] = 'is-valid' if link else 'is-invalid'
            return render(request, 'dashboards/user/events/create_exercise.html', context)

    return render(request, 'dashboards/user/events/create_exercise.html', context)


@login_required(login_url='login')
def edit_exercise(request, eid):
    events = Event.objects.all()[:4]

    exercise = Exercise.objects.get(id=eid)
    context = {'options': EXERCISES_NAV,
               'events': events, 'exercise': exercise}

    if request.POST:
        title = request.POST['title']
        reps = request.POST['reps']
        desc = request.POST['desc']
        link = request.POST['link']

        if title and reps and desc and link:
            exercise.title = title
            exercise.reps = reps
            exercise.desc = desc
            exercise.link = link
            exercise.save()
            return redirect('userdashboard-exercise-details', eid=eid)
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['repsValid'] = 'is-valid' if reps else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['linkValid'] = 'is-valid' if link else 'is-invalid'
            return render(request, 'dashboards/user/events/edit_exercise.html', context)

    return render(request, 'dashboards/user/events/edit_exercise.html', context)


@login_required(login_url='login')
def edit_routine(request, rid):
    events = Event.objects.all()[:4]

    r = get_object_or_404(Routine, id=rid)
    ex = Exercise.objects.all()
    context = {'options': ROUTINES_NAV,
               'events': events, 'routine': r, 'exercises': ex}
    context['days'] = ['Monday', 'Tuesday', 'Wednesday',
                       'Thursday', 'Friday', 'Saturday', 'Sunday']

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
            return redirect('userdashboard-routine-details', rid=rid)
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['daysValid'] = 'is-valid' if days else 'is-invalid'
            context['exercisesValid'] = 'is-valid' if exercises_list else 'is-invalid'

            return render(request, 'dashboards/user/events/edit_routine.html', context)

    return render(request, 'dashboards/user/events/edit_routine.html', context)


@login_required(login_url='login')
def create_routine(request):
    events = Event.objects.all()[:4]

    context = {'options': ROUTINES_NAV,
               'events': events, 'exercises': Exercise.objects.all()}
    context['days'] = ['Monday', 'Tuesday', 'Wednesday',
                       'Thursday', 'Friday', 'Saturday', 'Sunday']
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
            return redirect('userdashboard-routines')
        else:
            context['error'] = 'Please fill in all fields!'
            context['titleValid'] = 'is-valid' if title else 'is-invalid'
            context['descValid'] = 'is-valid' if desc else 'is-invalid'
            context['daysValid'] = 'is-valid' if days else 'is-invalid'
            context['exercisesValid'] = 'is-valid' if exercises_list else 'is-invalid'

            return render(request, 'dashboards/user/events/create_routine.html', context)

    return render(request, 'dashboards/user/events/create_routine.html', context)
