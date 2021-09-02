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
    ('7AM - 10AM','7AM - 10AM'),
    ('11AM - 2PM', '11AM - 2PM'),
    ('3PM - 6PM','3PM - 6PM'),
    ('7PM - 10PM','7PM - 10PM'),
)
Day_CHOICES = (
    ('Sunday','Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday','Tuesday'),
    ("Wednesday", "Wednesday"),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
)

class Hall(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Now_Showing, through='Movie_Hall')

    def __str__(self):
        return self.name


class Movie_Hall(models.Model):
    movie = models.ForeignKey(Now_Showing, related_name="movie", on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, related_name="hall", on_delete=models.CASCADE)
    time = models.CharField(max_length=100, choices=Time_CHOICES, default="7PM - 10PM'")
    day = models.CharField(max_length=100, choices=Day_CHOICES, default="Sunday")

    def __str__(self):
        return self.movie.name
