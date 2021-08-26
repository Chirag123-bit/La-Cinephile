from django.db import models



class User(models.Model):
    f_name = models.CharField(max_length=20)
    m_name = models.CharField(max_length=20, null=True, blank=True)
    l_name = models.CharField(max_length=20)
    profile = models.ImageField(upload_to ='uploads/')
    email = models.EmailField()
    password = models.CharField(max_length=30)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    date_created = models.DateField(auto_created=True, auto_now=True)


    def __str__(self):
        if self.m_name != None:
            return self.f_name+" "+self.m_name+" "+self.l_name
        return self.f_name+" "+self.l_name


