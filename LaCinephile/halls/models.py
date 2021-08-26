from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    color_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Hall(models.Model):
    h_Name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.h_Name

