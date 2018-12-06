from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

SEX_CHOICE = [("M", "Male"), ("F", "Female"), ('O', "Other")]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    sex = forms.CharField(label='What is your sex?', widget=forms.Select(choices=SEX_CHOICE))
    birth_date = forms.DateField(help_text='Required. Format: MM-DD-YYYY')

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'sex', 'birth_date', 'image', 'publisher']
