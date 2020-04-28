from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post, Category

#from blog.forms import ContactUs

# Create your views here.
def index(request, *args, **kwargs):
    #Search Function
    if request.method == "POST":
        search = request.POST['title']
        posts = Post.objects.filter(title__contains = search)
        category = Category.objects.all()
        return render(request, "blog/index.html", context={'posts':posts, 'category':category})

    # For rendering all cards
    else:
        posts = Post.objects.filter(status='P')
        category = Category.objects.all()
        return render(request, 'blog/index.html', context={'posts':posts, 'category':category})


def post_detail(request, id, *args, **kwargs):
    try:
        p_detail = Post.objects.get(id=id)
        return render(request, "blog/detail.html", context = {"p_detail":p_detail})
    except:
        return HttpResponse("Invalid Id")


def cat_view(request, category, *args, **kwargs):
    if request.method == "POST":
        search = request.POST['title']
        posts = Post.objects.filter(title__contains = search)
        category = Category.objects.all()
        return render(request, "blog/index.html", context={'posts':posts, 'category':category})
    try:

        if category == "All":
            posts = Post.objects.all()
            category = Category.objects.all()
            return render(request, "blog/category.html", context = {'posts':posts, 'category':category})

        else:
            posts = Post.objects.filter(category__name = category)
            category = Category.objects.all()   
            return render(request, "blog/category.html", context = {'posts':posts, 'category':category})
    except:
        return HttpResponse("Invalid category")



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

from blog.forms import AddBlog

def model_form_view(request, *args, **kargs):
    form = AddBlog()
    if request.method == "GET":
        form = AddBlog()
        return render(request, 'blog/modelform.html', context = {'form':form})

    else:
        form = AddBlog(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you")
        else:
            return render(request, 'blog/modelform.html', context = {'form':form})

def post_edit_form_view(request, id, *args, **kwargs):
    try:
        post = Post.objects.get(id = id)
    except:
        return HttpResponse("Invalid ID")

    if request.method == 'GET':
        form = AddBlog(instance = post)
        return render(request, 'blog/modelform.html', context = {'form':form})

    else:
        form = AddBlog(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you")
        else:   
            return render(request, 'blog/modelform.html', context = {'form':form})
        


###########################################################################################################
###########################################################################################################





###########################################################################################################

            # Search view

###########################################################################################################

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