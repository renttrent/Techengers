from django.shortcuts import redirect, render


def home(request):
    if request.user.is_anonymous == True:
        return redirect('welcome-page')
    else:
        return render(request, 'dashboards/userdashboard.html')
