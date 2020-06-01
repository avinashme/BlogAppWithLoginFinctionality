from django.contrib import admin
from blog.models import Post, Category
from account.models import Request

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Request)
