from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.core.validators import *


class User(models.Model):
    first_name = models.CharField(max_length=20, validators=[validators.MinLengthValidator(3)])
    last_name = models.CharField(max_length=20,validators=[validators.MinLengthValidator(3)])
    user_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(validators=[validate_email])
    password = models.CharField(max_length=30,validators=[validators.MinLengthValidator(8)])
    date_created = models.DateField(auto_created=True, auto_now=True, null=True)

    def __str__(self):
        if self.m_name != None:
            return self.f_name+" "+self.m_name+" "+self.l_name
        return self.f_name+" "+self.l_name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True, validators=[validators.MinLengthValidator(3)])
    pic = models.ImageField(upload_to ='uploads/profile', null=True, default="static/images/sample_user.png", validators=[validate_image_file_extension])
    phone = models.CharField(max_length=10, null=True,validators=[validators.MinLengthValidator(7)])
    

