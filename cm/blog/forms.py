from django import forms
import re

# Contact Us Form
    # Name
    # Email
    # Phone Number
    # Message
    # Country
    # Submit Button

########################################################################################################

#                                 Normal Form

########################################################################################################


# class ContactUs(forms.Form):
#     countries = [('IND','INDIA'), ("CH",'CHINA')]

#     name = forms.CharField(max_length = 50, initial="Name", widget=forms.TextInput(attrs={'class' : 'name-field'}))
#     email = forms.EmailField(required=False)
#     phone_no = forms.RegexField(regex = "^[6-9][0-9]{9}$", required=False, label="Phone")
#     message = forms.CharField(max_length=500, widget=forms.Textarea)
#     country = forms.ChoiceField(choices = countries)
#     password = forms.CharField(max_length=16, widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         phone = cleaned_data['phone_no']
#         email = cleaned_data['email']

#         if phone == '' and email == '':
#             #raise forms.ValidationError("Email or Phone 1 should be field", code='invalid')
#             self.add_error("phone_no", "Email or Phone 1 should be field")

#     def clean_password(self):
#         password = self.cleaned_data['password']
#         r = re.search('[A-Z][a-z][0-9]', password)

#         if not r:
#             raise forms.ValidationError("1 Upper, 1Lower, 1Special 1Num", code="upper")
#         else:
#             return password



###########################################################################################################
###########################################################################################################






###########################################################################################################

##                                  Model Form
###########################################################################################################

from django.forms import ModelForm
from blog.models import Post

class AddBlog(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'category', 'author', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image.size > 2000000:
            raise forms.ValidationError("Image Size Should less than 200KB", code='size')
        else:
            return image
