from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

from .models import Profile
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
    user = User.objects.get(pk=pk)
    form = UserProfile(instance=user)
    ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('gender', 'bio',
                                                                        'location', 'birthday', 'website'))
    formset = ProfileInlineFormset(instance=user)
    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == 'POST':
            form = UserProfile(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
            if form.is_valid():
                create_user = form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=create_user)
                if formset.is_valid():
                    create_user.save()
                    formset.save()
                    return render(request, 'users/profile_view.html')
        return render(request, 'users/profile_edit.html', {
            'noodle': pk,
            'noodle_form': form,
            'formset': formset,
        })
    else:
        raise PermissionDenied


def show_profile(request):
    return render(request, 'users/profile_view.html')
