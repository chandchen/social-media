from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # nickname = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=100, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
