from django.db import models
from django.contrib.auth.models import User



class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    date_created = models.DateField(auto_created=True, auto_now=True, null=True)

    def __str__(self):
        if self.m_name != None:
            return self.f_name+" "+self.m_name+" "+self.l_name
        return self.f_name+" "+self.l_name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    pic = models.ImageField(upload_to ='uploads/profile', null=True, default="static/images/sample_user.png")
    phone = models.CharField(max_length=10, null=True)
    

