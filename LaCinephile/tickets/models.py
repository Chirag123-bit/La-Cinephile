from django.db import models
from django.db.models.fields import BooleanField, IntegerField
from django.contrib.auth.models import User
from halls.models import Movie_Hall 

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)
    discount = IntegerField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie_Hall, related_name='+', on_delete=models.CASCADE)
    seats = models.TextField(null=True)
    discount = models.ForeignKey(Categories, related_name='+', on_delete=models.CASCADE)
