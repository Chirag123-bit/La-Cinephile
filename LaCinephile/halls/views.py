from django.shortcuts import render
from .models import Category
from tickets.models import Categories as ticket
from movies.models import Now_Showing
from halls.models import Hall
from django.http import JsonResponse
from halls.models import Movie_Hall

# Create your views here.

def prices(request):
    hall_cat = Category.objects.all()
    ticket_cat = ticket.objects.all()
    context={
        'activate_prices':'active',
        'hall_cat':hall_cat,
        'ticket_cat':ticket_cat
    }
    return render(request, 'halls/price.html',context)


def book(request):
    mh = Movie_Hall.objects.all()
    context={
        'activate_book':'active',
        'mh':mh
    }
    return render(request, 'halls/reservation.html',context)


def movie_json(request):
    movies = list(Now_Showing.objects.values())
    return JsonResponse({'data':movies})

def hall_json(request, *args, **kwargs):
    selected_movie = kwargs.get('movie')
    obj_model = Movie_Hall.objects.values('id', 'hall__name', 'hall__category__name').filter(movie__id=selected_movie)
    print(obj_model)
    resp=[]
    for i in obj_model:
        print(i['id'])
        di = {
            "id":i['id'],
            "hall":i['hall__name'],
            "cat":i['hall__category__name']
        }
        resp.append(di)
    return JsonResponse({'data':resp})


def day_json(request, *args, **kwargs):
    selection = kwargs.get('id')
    obj_model = Movie_Hall.objects.values('id', 'day').filter(movie__id=selection)
    print(obj_model)
    resp=[]
    for i in obj_model:
        print(i['id'])
        di = {
            "id":i['id'],
            "day":i['day'],
        }
        resp.append(di)
    return JsonResponse({'data':resp})


# def test(request):
#     mh = Movie_Hall.objects.all()
#     movies = Now_Showing.objects.all()
#     # print(movies)
#     for i in mh:
#         print(i.movie.name)
#         print(i.hall.h_Name)
#     context={
#         'mh':mh
#     }
#     return render(request, 'halls/test.html',context)



