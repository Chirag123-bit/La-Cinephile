from django.shortcuts import render
from halls.models import Ticket, Purchase

def detail(request, uid, mid):
    movies = Ticket.objects.filter(user__id = uid, movie__id=mid)
    purchase = Purchase.objects.filter(user__id = uid, movie__id=mid)
    seats=[]
    price = int((purchase.values()[0])["price"])
    for i in movies:
        seats.append(i.seats)
    
    context = {
        'movies':movies[0],
        'seats':seats,
        'activate_movies':"active"
    }
    if(len(purchase))>0:
        price *= len(purchase)
        context = {
        'movies':movies[0],
        'seats':seats,
        'purchase':True,
        'price':price,
        'activate_movies':"active"
    }

    return render(request,'tickets/ticket_details.html',context)

