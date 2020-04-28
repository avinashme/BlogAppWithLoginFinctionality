from django.contrib import admin
from django.urls import path, re_path, include

from blog.views import index, post_detail, cat_view
# from blog.view import contact_view

from blog.views import model_form_view 
from blog.views import post_edit_form_view
# from blog.views import search_view




urlpatterns = [
    path('', index),
    path('<int:id>', post_detail),
    #path('contact', contact_view),
    path('modelform', model_form_view),
    #path('', search_view),
    path('modelform/<int:id>', post_edit_form_view),
    path('<str:category>', cat_view),
    
]