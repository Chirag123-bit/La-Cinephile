from django.shortcuts import render
from .models import Now_Showing, Up_Comming
from accounts.auth import user_only
from halls.models import Movie_Hall, Ticket
from django.db.models import Count
from django.contrib.auth.decorators import  login_required

@user_only
def home(request):
    """Renders the home page for now showing movies"""
    movies = Now_Showing.objects.all()
    context = {
        'movies':movies,
        'activate_home':"active"
    }

    return render(request,'movies/home.html',context)

@user_only
def movies(request):
    """Renders the movie page with now showing and up-comming movies"""
    movies = Now_Showing.objects.all()
    umovies = Up_Comming.objects.all()
    context = {
        'movies':movies,
        'umovies':umovies,
        'activate_movies':"active"
    }

    return render(request,'movies/movies.html',context)

@user_only
def show(request, id):
    """Renders the movie page with now showing movies"""
    movie = Now_Showing.objects.get(id=id)
    context = {
        'movie' : movie,
        'activate_movies':"active",
    }
    return render(request, 'movies/now_showing.html', context)


@user_only
def up_show(request, id):
    """Renders the movie page with Up-comming movies"""
    movie = Up_Comming.objects.get(id=id)
    context = {
        'movie' : movie,
        'activate_movies':"active",
    }
    return render(request, 'movies/up_comming.html', context)

@login_required
@user_only
def user_movies(request):
    """Renders the dashboard page with user-purchased/booked movies"""
    id = request.user.id
    movies = Ticket.objects.filter(user__id = id).values('movie__id').all().distinct()
    
    i = 1
    id = movies[0]['movie__id']
    res = Movie_Hall.objects.filter(id=id)

    while(i<len(movies)):
        id = movies[i]['movie__id']
        res |= Movie_Hall.objects.filter(id=id)
        i+=1

    context = {
        'movies':res,
        'activate_movies':"active"
    }

    return render(request,'accounts/dashboard.html',context)

