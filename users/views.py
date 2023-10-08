from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Profile, Follow
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm


# Create your views here.
def user_profile(request):
    profiles = request.user.profile
    context = {'profiles': profiles}
    return render(request, 'users/profile.html', context)

def single_user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    login_user = request.user.profile


    context = {'profile': profile, 'login_user': login_user, 'request':
        request}
    return render(request, 'users/single_users_profile.html', context)

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

# def follow_profile(request, pk):
#     followers = Profile.objects.get(id=pk)
#     request.user.profile.following.add(followers)
#     return redirect(request, 'users/profile.html')

def follow_profile(request, pk):
    following = Profile.objects.get(id=pk)
    existing_user = Follow.objects.filter(follower=request.user.profile,
                                          followed=following)
    if not existing_user.exists():
        follow_instance = Follow(follower=request.user.profile, followed=following)
        follow_instance.save()
    return redirect('single-profile', pk=pk)

def unfollow_profile(request, pk):
    unfollowing = Profile.objects.get(id=pk)
    Follow.objects.filter(follower=request.user.profile,
                          followed=unfollowing).delete()
    return redirect('single-profile', pk=pk)

def follow_users(request, pk):
    profile = Profile.objects.get(id=pk)
    followers = Follow.objects.filter(followed=profile)

    context = {'followers': followers, 'profile': profile}
    return render(request, 'users/followers.html', context)

def following_user(request, pk):
    profile = Profile.objects.get(id=pk)
    following = Follow.objects.filter(follower=profile)
    context = {'following': following, 'profile': profile}
    return render(request, 'users/following.html', context)



