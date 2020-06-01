from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Category
from account.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.forms import PostForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

# Create your views here.

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status="P")
    template_name = "blog/index.html"
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


# We do not define out context object name here by defualt it is model name.
class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = Post
    queryset = Post.objects.filter(status = "P")
    template_name = 'blog/detail.html'
   

class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "blog/index.html"
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['category'] == "All":
            context['posts'] = Post.objects.all()
            return context
        else:
            context['posts'] = Post.objects.filter(category__name = self.kwargs['category'])
            return context



###########################################################################################################

            # Form Here

###########################################################################################################


class PostFormCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    login_url = "login"
    permission_required = "blog.add_post"
    form_class = PostForm
    template_name = 'blog/create_post.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'initial':{'author': self.request.user}})
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = "login"
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'

    def test_func(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        post = Post.objects.get(slug=slug)
        if self.request.user == post.author:
            return True
        else:
            return False
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'initial':{'author': self.request.user}})
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin,DeleteView):
    login_url = "login"
    permission_required = "blog.delete_post"
    model = Post
    success_url = "/blogs"

    def test_func(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        post = Post.objects.get(slug=slug)
        if self.request.user == post.author:
            return True
        else:
            return False
    


###########################################################################################################

            # Search view

###########################################################################################################


class SearchListView(ListView):
    model = Post
    template_name = "blog/search.html"
    context_object_name = 'posts'

    def get_queryset(self, **kwargs):
        if self.request.method == 'GET':
            posts = Post.objects.filter(title__contains = self.request.GET['title'])
            return posts


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context