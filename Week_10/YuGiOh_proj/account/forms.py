from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form, ModelForm, PasswordInput
from django import forms
from .models import Profile


class UserSignupForm(UserCreationForm):
    model = User
    fields = ['username','password']
        
        
class ChangePictureForm(Form):
    picture = forms.URLField()
    
    
class ChangePasswordForm(Form):
    old_password = forms.CharField(widget=PasswordInput(attrs={'class':'col-md-4 col-sm-4'}))
    new_password = forms.CharField(widget=PasswordInput(attrs={'class':'col-md-4 col-sm-4'}))
    confirm_new_password = forms.CharField(widget=PasswordInput(attrs={'class':'col-md-4 col-sm-4'}))