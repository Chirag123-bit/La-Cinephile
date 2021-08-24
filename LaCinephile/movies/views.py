from django.shortcuts import render
from .models import Movie, Now_Showing, Up_Comming

# Create your views here.

def home(request):
    movies = Now_Showing.objects.all()
    context = {
        'movies':movies,
        'activate_home':"active"
    }

    return render(request,'movies/home.html',context)

def movies(request):
    movies = Now_Showing.objects.all()
    umovies = Up_Comming.objects.all()
    context = {
        'movies':movies,
        'umovies':umovies,
        'activate_movies':"active"
    }

    return render(request,'movies/movies.html',context)


def show(request, id):
    movie = Now_Showing.objects.get(id=id)
    context = {
        'movie' : movie,
        'activate_movies':"active",
    }
    return render(request, 'movies/now_showing.html', context)




