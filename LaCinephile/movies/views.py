from django.shortcuts import render
from .models import Now_Showing, Up_Comming
from accounts.auth import user_only
from halls.models import Movie_Hall, Ticket
from django.db.models import Count
from django.contrib.auth.decorators import  login_required

@user_only
def home(request):
    movies = Now_Showing.objects.all()
    context = {
        'movies':movies,
        'activate_home':"active"
    }

    return render(request,'movies/home.html',context)

@user_only
def movies(request):
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
    movie = Now_Showing.objects.get(id=id)
    context = {
        'movie' : movie,
        'activate_movies':"active",
    }
    return render(request, 'movies/now_showing.html', context)


@user_only
def up_show(request, id):
    movie = Up_Comming.objects.get(id=id)
    context = {
        'movie' : movie,
        'activate_movies':"active",
    }
    return render(request, 'movies/up_comming.html', context)

@login_required
@user_only
def user_movies(request, id):

    movies = Ticket.objects.filter(user__id = id).values('movie__id').distinct()
    
    res=[]
    for i in movies:
        id = i['movie__id']
        mv = Movie_Hall.objects.filter(id=id)
        res.append(mv)
    context = {
        'movies':mv,
        'activate_movies':"active"
    }
    print(res)

    return render(request,'accounts/dashboard.html',context)

