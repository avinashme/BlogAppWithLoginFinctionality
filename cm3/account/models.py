from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to="profile/", blank=True)
    is_author = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class Request(models.Model):
    statuses = [
        ("T", "True"),
        ("F", "False"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_author = models.CharField(max_length=1, choices=statuses)

    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):
        if self.is_author == "T":
            author_grp = Group.objects.get(name="Author")
            self.user.groups.add(author_grp)
            return super().save(*args, **kwargs)
        else:
            return super().save(*args, **kwargs)