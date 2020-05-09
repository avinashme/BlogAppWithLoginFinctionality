from django.contrib import admin
from django.urls import path, re_path, include
from account.views import UserCreateView, ProfileDetailView
from account.views import ProfileUpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('signup', UserCreateView.as_view(), name = 'signup'),
    path('login/', LoginView.as_view(template_name = "account/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileDetailView.as_view()),
    path('profile/edit/<int:pk>', ProfileUpdateView.as_view()),
    # path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    
]
