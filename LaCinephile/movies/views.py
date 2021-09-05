from django.shortcuts import render
from .models import Now_Showing, Up_Comming
from accounts.auth import user_only
from halls.models import Ticket
from django.db.models import Count


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


@user_only
def user_movies(request, id):

    movies = Ticket.objects.filter(user__id = id).values('movie__movie__id').distinct()
    mv = Now_Showing.objects.all().values()

    temp = []
    for i in movies:
        temp.append(i["movie__movie__id"])

    res=[]
    for i in mv:
        if i['id'] in temp:
            res.append(i)

    context = {
        'movies':res,
        'activate_movies':"active"
    }

    return render(request,'accounts/dashboard.html',context)

