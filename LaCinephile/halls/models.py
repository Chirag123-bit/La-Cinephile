from datetime import datetime
from tickets.models import Categories
from django.db import models
from movies.models import Now_Showing
from django.contrib.auth.models import User
import datetime
from django.core import validators

class Category(models.Model):#model to create hall category
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
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
    movies = models.ManyToManyField(Now_Showing, through='Movie_Hall', blank=True)

    def __str__(self):
        return self.name


class Movie_Hall(models.Model):
    movie = models.ForeignKey(Now_Showing, related_name="movie", on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, related_name="hall", on_delete=models.CASCADE)
    time = models.CharField(max_length=100, choices=Time_CHOICES, default="7PM - 10PM")
    date = models.DateField( default=datetime.date.today)
    discount = models.BooleanField(default=True)
    booked = models.ManyToManyField(User, through="Ticket", blank=True)

    def __str__(self):
        return self.movie.name + " In " + self.hall.name +" ( " + str(self.date) + " " + str(self.time) + " )"

ticket_choices = (
    ("Purchased", "Purchased"),
    ("Canceled", "Canceled"),
    ("Booked","Booked")
)

class TicketTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True) #Indexing for user table
    movie = models.ForeignKey(Movie_Hall, on_delete=models.CASCADE)
    discount = models.ForeignKey(Categories, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=ticket_choices, default="Booked")

    class Meta:
        abstract = True

class Ticket(TicketTemplate):
    seats = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.movie.movie.name

class Purchase(TicketTemplate):
    seats = models.CharField(max_length=100, null=True)
    price = models.IntegerField()
    payment_completed = models.BooleanField(default=False)




