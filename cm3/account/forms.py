from django.forms import ModelForm
from django import forms
from account.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView


# from account.models import Profile
class SignUpForm(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(ModelForm): 
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'bio', 'image']