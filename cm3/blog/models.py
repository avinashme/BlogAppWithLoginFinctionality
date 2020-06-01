from django.db import models
from account.models import User
from django.utils.text import slugify
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    statuses = [
        ("D", "Draft"),
        ("P", "Publish"),
    ]
    title = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 50, unique=True, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=1, choices = statuses)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/post')
    date = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'slug':self.slug})