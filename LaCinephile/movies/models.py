from django.db import models
from django.core import validators

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50, validators=[validators.MinLengthValidator(1)])
    poster = models.ImageField(upload_to = 'static/images/movies')
    trailer = models.URLField()
    summary = models.CharField(max_length=500, validators=[validators.MinLengthValidator(10)])
    desc = models.TextField(default="Summary", validators=[validators.MinLengthValidator(10)])
    actors = models.CharField(max_length=300, validators=[validators.MinLengthValidator(5)])
    director = models.CharField(max_length=100, validators=[validators.MinLengthValidator(5)])
    background = models.ImageField(upload_to = 'static/images/movies',null=True)

    def __str__(self):
        return self.name


    class Meta:
        abstract = True


class Now_Showing(Movie):
    imdb = models.FloatField()


class Up_Comming(Movie):
    release_date = models.CharField(max_length=50)
    external_site = models.URLField(null=True)




