from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm


# Create your views here.
def user_profile(request):
    profiles = request.user.profile
    context = {'profiles': profiles}
    return render(request, 'users/profile.html', context)

def edit_profile(request):
    profiles = request.user.profile
    form = ProfileForm(instance=profiles)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profiles)
        if form.is_valid():
            form.save()
        return redirect('profile')
    context = {'form': form}
    return render(request, 'users/edit_profile.html', context)


def login_page(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            print('not a user')

    context = {'page': page}
    return render(request, 'users/registration.html', context)

def registration_page(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    context = {'page': page, 'form': form}
    return render(request, 'users/registration.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')