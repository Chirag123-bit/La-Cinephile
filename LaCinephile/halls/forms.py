from django.db.models import fields
from .models import Hall, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.forms import ModelForm

class HallForm(ModelForm):
    class Meta:
        model = Hall
        fields = "__all__"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"