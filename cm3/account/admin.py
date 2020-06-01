# from django.contrib import admin
# from account.models import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User


# Register your models here.
admin.site.register(User, UserAdmin)


# admin.site.register(Profile)