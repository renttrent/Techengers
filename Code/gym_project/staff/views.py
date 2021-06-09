from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from dashboards.models import Event, Exercise, Routine
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url='login')
@staff_member_required
def home(request):
    return redirect('staff-latest-activity')


@login_required(login_url='login')
@staff_member_required
def latest_activity(request):
    # navigation = {
    #     'schedule': {
    #         'name': 'Schedule',
    #         'isActive': True,
    #         'url': 'schedule'
    #     },
    #     'exercises': {
    #         'name': 'Exercises',
    #         'isActive': False,
    #         'url': 'exercises'
    #     },
    #     'routines': {
    #         'name': 'Routines',
    #         'isActive': False,
    #         'url': 'routines'
    #     },
    #     'diets': {
    #         'name': 'Selected Diets',
    #         'isActive': False,
    #         'url': 'diets'
    #     },
    #     'trainers': {
    #         'name': 'Trainers',
    #         'isActive': False,
    #         'url': 'trainers'
    #     },
    # }
    # events = Event.objects.all()[:4]

    # schedule = Routine.objects.filter(owner=request.user)

    # context = {'options': navigation, 'events': events, 'schedule': schedule}
    return render(request, 'staff/base.html')
