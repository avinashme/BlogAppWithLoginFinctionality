from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from account.forms import SignUpForm, ProfileUpdateForm 
from account.models import User
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


# Create your views here.
class UserCreateView(CreateView):
    template_name = 'account/signup.html'
    form_class =  SignUpForm
    success_url = "/blogs"


class ProfileDetailView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,DetailView):
    login_url = "login"
    permission_required = "account.view_user"
    model = User
    template_name = "account/profile_detail.html"
    context_object_name = 'user'

    def test_func(self, *args, **kwargs):
        url_user = User.objects.get(id=self.kwargs.get('pk'))
        if self.request.user == url_user:
            return True
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author__username= context['user']) 
        return context


class ProfileUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url = "login"
    model = User
    form_class = ProfileUpdateForm
    template_name = 'account/profile_edit.html'
    success_url = "/accounts/profile/update/done"

    
    def test_func(self, *args, **kwargs):
        url_user = User.objects.get(id=self.kwargs.get('pk'))
        if self.request.user == url_user:
            return True
        else:
            return False



class ProfileUpdateDoneView(LoginRequiredMixin, ListView):
    login_url = "login"
    model = User
    template_name = 'account/profile_update_done.html'
