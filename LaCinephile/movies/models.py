from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    poster = models.ImageField(upload_to = 'static/images/movies')
    trailer = models.URLField()
    imdb = models.FloatField()
    summary = models.CharField(max_length=500)
    desc = models.TextField(default="Summary")
    actors = models.CharField(max_length=300)
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.name



