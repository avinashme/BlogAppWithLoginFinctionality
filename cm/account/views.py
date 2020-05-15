from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from account.forms import SignUpForm, ProfileUpdateForm
from account.models import Profile
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class UserCreateView(CreateView):
    template_name = 'account/signup.html'
    form_class =  SignUpForm
    success_url = "/blogs"


class ProfileDetailView(LoginRequiredMixin,DetailView):
    login_url = "login"
    model = Profile
    template_name = "account/profile_detail.html"
    context_object_name = 'profile'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author__username= context['profile']) 
        return context

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'account/profile_edit.html'