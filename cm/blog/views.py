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

class PostFormCreateView(CreateView):
    form_class = PostForm
    template_name = 'blog/create_post.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blogs"
    



###########################################################################################################

            # Forms Here

###########################################################################################################


# def contact_view(request, *args, **kwargs):

#     if request.method == 'GET':
#         form = ContactUs()
#         return render(request, "blog/contact.html", context = {"form":form})
    
#     else:
#         form = ContactUs(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return HttpResponse("Thank you")
#         else:
#             return render(request, "blog/contact.html", context = {"form":form})
 


###########################################################################################################
###########################################################################################################





###########################################################################################################

            # Model Form

###########################################################################################################

# from blog.forms import AddBlog

# def model_form_view(request, *args, **kargs):
#     form = AddBlog()
#     if request.method == "GET":
#         form = AddBlog()
#         return render(request, 'blog/modelform.html', context = {'form':form})

#     else:
#         form = AddBlog(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Thank you")
#         else:
#             return render(request, 'blog/modelform.html', context = {'form':form})

# def post_edit_form_view(request, id, *args, **kwargs):
#     try:
#         post = Post.objects.get(id = id)
#     except:
#         return HttpResponse("Invalid ID")

#     if request.method == 'GET':
#         form = AddBlog(instance = post)
#         return render(request, 'blog/modelform.html', context = {'form':form})

#     else:
#         form = AddBlog(request.POST, request.FILES, instance = post)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Thank you")
#         else:   
#             return render(request, 'blog/modelform.html', context = {'form':form})
        


###########################################################################################################
###########################################################################################################


###########################################################################################################
###########################################################################################################








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


# def search_view(request, *args, **kargs):
#     if request.method == "GET":
#         print(request.GET)
#         return render(request, "blog/index.html")
        
#     else:
#         if request.method == "POST":
#             print(request.POST)
#             search = request.POST['title']
#             posts = Post.objects.filter(title__contains = search)
#             print(posts)
#             #posts = Post.objects.filter(author__contains = search)  
#             return render(request, "blog/index.html", context={'posts':posts})
#         else:
#             return HttpResponse("Invalid Blog title")



###########################################################################################################
###########################################################################################################





###########################################################################################################

            # 

###########################################################################################################