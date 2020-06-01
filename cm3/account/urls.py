from django.contrib import admin
from django.urls import path, re_path, include
from account.views import UserCreateView, ProfileDetailView
from account.views import ProfileUpdateView, ProfileUpdateDoneView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('signup', UserCreateView.as_view(), name = 'signup'),
    path('login/', LoginView.as_view(template_name = "account/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password-reset/', PasswordResetView.as_view(template_name="account/password_reset_form.html", email_template_name='account/password_reset_email.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='account/password_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='account/password_done.html'), name='password_reset_complete'),
    
    path('password-change/', PasswordChangeView.as_view(template_name="account/password_change.html"), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name='password_change_done'),

    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view()),
    path('profile/update/done', ProfileUpdateDoneView.as_view()),
    
]
