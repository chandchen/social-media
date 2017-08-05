from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UserForm, UserProfile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def edit_profile(request, pk):
    if request.method == 'POST':
        profile_form = UserProfile(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            photo = request.user.profile.photo
            return render(request, 'users/profile_view.html', {'photo': photo})
    else:
        profile_form = UserProfile(instance=request.user.profile)
    return render(request, 'users/profile_edit.html', {'form': profile_form})


def show_profile(request):
    profile = request.user.profile
    return render(request, 'users/profile_view.html', {'photo': profile.photo})
