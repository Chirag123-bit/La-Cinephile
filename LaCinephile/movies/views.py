from django.shortcuts import render
from .models import Movie

# Create your views here.

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
        'activate_home':"active"
    }

    return render(request,'movies/home.html',context)

def movies(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
        'activate_movies':"active"
    }

    return render(request,'movies/movies.html',context)
