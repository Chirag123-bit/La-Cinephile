from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)
    discount = IntegerField()

    def __str__(self):
        return self.name
