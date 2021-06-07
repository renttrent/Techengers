from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}')
            return redirect('userdashboard')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'login/login.html', context)


def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created successfully. You can Log In {username}.')

            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'login/register.html', context)


def welcome(request):
    return render(request, 'login/welcome-page.html')
