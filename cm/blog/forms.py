from django import forms
import re
from django.forms import ModelForm
from blog.models import Post
from django.contrib.auth.models import User


# Contact Us Form
    # Name
    # Email
    # Phone Number
    # Message
    # Country
    # Submit Button

###########################################################################################################

#                                  Model Form
###########################################################################################################


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'category', 'author','image']

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image.size > 504800:
            raise forms.ValidationError("Image Size Should less than 2 MB", code='size')
        else:
            return image
