from django.db import models
from movies.models import Now_Showing

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    color_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name

Time_CHOICES = (
    ('1','7AM - 10AM'),
    ('2', '11AM - 2PM'),
    ('3','3PM - 6PM'),
    ('4','7PM - 10PM'),
)
Day_CHOICES = (
    ('1','Sunday'),
    ('2', 'Monday'),
    ('3','Tuesday'),
    ('4','Thursday'),
    ('4','Friday'),
    ('4','Saturday'),
)

class Hall(models.Model):
    h_Name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Now_Showing, through='Movie_Hall')

    def __str__(self):
        return self.h_Name


class Movie_Hall(models.Model):
    movie = models.ForeignKey(Now_Showing, related_name="movie", on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, related_name="hall", on_delete=models.CASCADE)
    time = models.CharField(max_length=100, choices=Time_CHOICES, default="1")
    day = models.CharField(max_length=100, choices=Day_CHOICES, default="1")

    def __str__(self):
        return self.movie.name
