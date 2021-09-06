from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.core.validators import *


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    profile_pic = models.FileField(upload_to='static/profiles', default='static/images//sample_user.png')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + " "+ self.lastname


# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
#     middle_name = models.CharField(max_length=20, null=True, blank=True, validators=[validators.MinLengthValidator(3)])
#     pic = models.ImageField(upload_to ='uploads/profile', null=True, default="static/images/sample_user.png", validators=[validate_image_file_extension])
#     phone = models.CharField(max_length=10, null=True,validators=[validators.MinLengthValidator(7)])
    

