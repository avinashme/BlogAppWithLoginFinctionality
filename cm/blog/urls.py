from django.contrib import admin
from django.urls import path, re_path, include
from blog.views import PostFormCreateView, PostUpdateView, PostDeleteView
# from blog.views import index, post_detail, cat_view
# from blog.view import contact_view

# from blog.views import model_form_view 
# from blog.views import post_edit_form_view

from blog.views import PostListView, PostDetailView ,CategoryListView
from blog.views import SearchListView
# from blog.views import search_view


urlpatterns = [
    path('', PostListView.as_view()),
    path('search', SearchListView.as_view()),
    path('posts', PostFormCreateView.as_view()),
    path('posts/<slug:slug>', PostDetailView.as_view(),name='detail'), 
    path('posts/<slug:slug>/update', PostUpdateView.as_view()),
    path('posts/<slug:slug>/delete', PostDeleteView.as_view(), name='delete'), 
    path('<str:category>', CategoryListView.as_view()),   
]
