from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Now_Showing, Up_Comming
from accounts.auth import user_only
from halls.models import Movie_Hall, Purchase, Ticket
from tickets.models import Categories
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
    if 'q' in request.GET:
        q=request.GET['q']
        movies = Now_Showing.objects.filter(name__icontains=q)
        umovies = Up_Comming.objects.filter(name__icontains=q)
        context = {
        'movies':movies,
        'umovies':umovies,
        'activate_movies':"active"
        }
        return render(request,'movies/movies.html',context)

    else:
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
    seats = Ticket.objects.filter(user__id=id).count()
    purchased = Purchase.objects.filter(user__id=id).values("price")
    discount = Purchase.objects.filter(user__id = id).values("discount_id")
    cat = Categories.objects.all().values("id", "discount")
    dis=[]
    dis_price = {}
    spent = 0
    disc = 0
    for i in discount:
        dis.append(i)

    for i in cat:
        dis_price[i['id']] = i['discount']

    for i in dis:
        disc += dis_price[int(i['discount_id'])]
        
    for i in purchased:
        spent += int(i['price'])
    
    i = 1
    res={}
    if(len(movies)>0):
        id = movies[0]['movie__id']
        res = Movie_Hall.objects.filter(id=id)

        while(i<len(movies)):
            id = movies[i]['movie__id']
            res |= Movie_Hall.objects.filter(id=id)
            i+=1

    context = {
        'movies':res,
        'movie_count': len(res),
        'activate_movies':"active",
        'seat_count':seats,
        'spent':spent,
        'disc':disc

    }

    return render(request,'accounts/dashboard.html',context)

