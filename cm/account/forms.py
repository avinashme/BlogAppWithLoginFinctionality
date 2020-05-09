from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models import Profile

class SignUpForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'image']