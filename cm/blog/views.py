from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Category
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.forms import PostForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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


# We not define out context object name here by defualt it is model name.
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

class PostFormCreateView(LoginRequiredMixin,CreateView):
    login_url = "login"
    form_class = PostForm
    template_name = 'blog/create_post.html'


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = "login"
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = "login"
    model = Post
    success_url = "/blogs"
    


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


