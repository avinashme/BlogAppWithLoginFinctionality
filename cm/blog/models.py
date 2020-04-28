from django.db import models


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
    content = models.TextField()
    status = models.CharField(max_length=1, choices = statuses)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog/post')

    def __str__(self):
        return self.title


    