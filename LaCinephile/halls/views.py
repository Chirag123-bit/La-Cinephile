from django.shortcuts import redirect, render
from .models import Category
from tickets.models import Categories as ticket
from movies.models import Now_Showing 
from halls.models import Ticket
from django.http import JsonResponse
from halls.models import Movie_Hall
import datetime
from tickets.models import Categories
import json 



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
    if request.method == "POST":
        data = request.POST
        user = request.user
        movie = data.get('mid')
        seats = data.get('seat_selected')
        discount = data.get('discountId')

        print(seats)

        mv = Movie_Hall.objects.filter(id=int(movie))[0]
        dis = Categories.objects.filter(id=int(discount))[0]

        ticket = Ticket(user=user, movie=mv, seats=seats, discount=dis)
        if ticket:
            i=0
            while(i<len(seats)):
                ticket = Ticket(user=user, movie=mv, seats=seats[i:i+2], discount=dis)
                ticket.save()
                i+=3
            return redirect("/")

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
    obj_model = Movie_Hall.objects.values('hall_id', 'hall__name', 'hall__category__name', 'hall__category__price').filter(movie__id=selected_movie)
    resp=[]
    for i in obj_model:
        di = {
            "id":i['hall_id'],
            "hall":i['hall__name'],
            "cat":i['hall__category__name'],
            'price':i['hall__category__price']
        }
        resp.append(di)
    return JsonResponse({'data':resp})


def date_json(request, *args, **kwargs):
    mselection = kwargs.get('mid')
    hselection = kwargs.get('hid')
    obj_model = Movie_Hall.objects.values('id', 'date').filter(movie__id=mselection, hall__id=hselection)
    resp=[]
    for i in obj_model:
        di = {
            "id":i['id'],
            "date":i['date'],
            "day":datetime.datetime.strptime(str(i['date']), '%Y-%M-%d').strftime('%A'),
        }
        resp.append(di)
    return JsonResponse({'data':resp})


def time_json(request, *args, **kwargs):
    mselection = kwargs.get('mid')
    hselection = kwargs.get('hid')
    day = kwargs.get('date')

    obj_model = Movie_Hall.objects.values('id', 'time', 'booked').filter(movie__id=mselection, hall__id=hselection, date=day)
    resp=[]

    for i in obj_model:
        di = {
            "id":i['id'],
            "time":i['time'],
        }
        resp.append(di)
    return JsonResponse({'data':resp})

def seats_json(request, *args, **kwargs):
    mh_id = kwargs.get("id")
    obj_model = Ticket.objects.values('seats').filter(movie__id=mh_id)
    resp=[]
    for i in obj_model:
        di = {
            "seat":i['seats'],
        }
        resp.append(di)
    return JsonResponse({'data':resp})


def dis_price_json(request, *args, **kwargs):

    field = Movie_Hall.objects.get(id=kwargs.get('hmid'))

    price = field.hall.category.price
    time = field.time
    day = datetime.datetime.strptime(str(field.date), '%Y-%M-%d').strftime('%A')
    dis_cat = 7

    if(field.discount==False):
        dis_cat=7

    elif(time=="7AM - 10AM"):
        dis_cat = 1

    elif(day=="Tuesday" or day=="Wednesday"):
        dis_cat = 6
    
    else:
        dis_cat=3
    
    if(dis_cat==7):
        discount=0
    else:
        ticket_cat = Categories.objects.get(id=dis_cat)
        discount = ticket_cat.discount
    data = [{"price":price-discount,"cat":dis_cat}]
    return JsonResponse({'data':data})




