from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import RegisterForm, UserForm, UserProfile

from django.views.generic import View, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib import messages


# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = RegisterForm()
#     return render(request, 'users/register.html', {'form': form})


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


# def show_profile(request, pk):
#     profile = request.user.profile
#     return render(request, 'users/profile_view.html', {'photo': profile.photo})


class ProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile_view.html'

    @classmethod
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        return render(request, self.template_name, {'profile': profile})


# @login_required
# def edit_profile(request, pk):
#     if request.method == 'POST':
#         profile_form = UserProfile(request.POST, request.FILES, instance=request.user.profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect('users:profile_view')
#     else:
#         profile_form = UserProfile(instance=request.user.profile)
#     return render(request, 'users/profile_edit.html', {'form': profile_form})


class ProfileEditView(LoginRequiredMixin, View):
    form_class = UserProfile
    template_name = 'users/profile_edit.html'

    @classmethod
    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user.profile)
        return render(request, self.template_name, {'form': form})

    @classmethod
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile_view', request.user.id)
        return render(request, self.template_name, {'form': form})


class PasswordChangeView(LoginRequiredMixin, View):
    template_name = 'users/change.html'

    @classmethod
    def get(self, request, *args, **kwargs):
        if request.user.has_usable_password():
            PasswordForm = PasswordChangeForm
        else:
            PasswordForm = AdminPasswordChangeForm
        form = PasswordForm(request.user)
        return render(request, self.template_name, {'form': form})

    @classmethod
    def post(self, request, *args, **kwargs):
        username = request.user.username
        if request.user.has_usable_password():
            PasswordForm = PasswordChangeForm
        else:
            PasswordForm = AdminPasswordChangeForm

        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(
                request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/users/change_done/')
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, self.template_name, {'form': form})


class PasswordChangeDoneView(LoginRequiredMixin, View):

    @classmethod
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'users/change_done.html')
