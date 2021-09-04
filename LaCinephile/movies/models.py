from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    poster = models.ImageField(upload_to = 'static/images/movies')
    trailer = models.URLField()
    summary = models.CharField(max_length=500)
    desc = models.TextField(default="Summary")
    actors = models.CharField(max_length=300)
    director = models.CharField(max_length=100)
    background = models.ImageField(null=True)

    def __str__(self):
        return self.name


    class Meta:
        abstract = True


class Now_Showing(Movie):
    imdb = models.FloatField()


class Up_Comming(Movie):
    release_date = models.CharField(max_length=50)
    external_site = models.URLField(null=True)
