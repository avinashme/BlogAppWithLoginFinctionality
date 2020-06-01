from django.contrib import admin
from django.urls import path, re_path, include
from blog.views import PostFormCreateView, PostUpdateView, PostDeleteView
from blog.views import PostListView, PostDetailView ,CategoryListView
from blog.views import SearchListView


urlpatterns = [
    path('', PostListView.as_view()),
    path('search', SearchListView.as_view()),
    path('posts', PostFormCreateView.as_view(),name='create_post'),
    path('posts/<slug:slug>', PostDetailView.as_view(),name='detail'), 
    path('posts/<slug:slug>/update', PostUpdateView.as_view(), name='update'),
    path('posts/<slug:slug>/delete', PostDeleteView.as_view(), name='delete'), 
    path('<str:category>', CategoryListView.as_view()),   
]


