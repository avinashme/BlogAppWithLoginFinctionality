from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from account.forms import SignUpForm, ProfileUpdateForm
from account.models import Profile


# Create your views here.
class UserCreateView(CreateView):
    template_name = 'account/signup.html'
    form_class =  SignUpForm
    success_url = "/blogs"


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "account/profile_detail.html"
    context_object_name = 'profile'   

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'account/profile_edit.html'

