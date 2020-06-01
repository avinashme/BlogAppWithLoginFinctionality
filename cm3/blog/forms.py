from django import forms
import re
from django.forms import ModelForm
from blog.models import Post
from account.models import User


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

    author = forms.CharField(disabled=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'category','image']


    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image.size > 504800:
            raise forms.ValidationError("Image Size Should less than 2 MB", code='size')
        else:
            return image
