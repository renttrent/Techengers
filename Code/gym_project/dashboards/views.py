from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, 'dashboards/user/dashboard.html')
