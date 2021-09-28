from django.core import validators
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.forms import ModelForm


#Account's Form
class UserForm(UserCreationForm):
    """Form for creating Users"""
    class Meta:
        model = User
        first_name =  forms.CharField(max_length=50, validators=[validators.MinLengthValidator(3)])
        lastname = forms.CharField(max_length=50, validators=[validators.MinLengthValidator(3)])
        email = forms.EmailField(validators=[validators.EmailValidator])
        username = forms.CharField(validators=[validators.MinLengthValidator(3)])
        fields = ['first_name', 'last_name','email','username']

class LoginForm(forms.Form):
    """Form to allow users to log in"""
    username = forms.CharField(validators=[validators.MinLengthValidator(3)])
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(ModelForm):
    """Form for creating User profile"""
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user', 'email', 'username']
        

        

class EditUserProfileForm(UserChangeForm):
    """Form for allowing users to edit their profile"""
    class Meta:
        model = Profile
        fields= "__all__"



