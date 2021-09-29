from django.shortcuts import render, redirect
from halls.models import Ticket, Purchase
from django.db.models import Q

def detail(request, uid, mid):
    """
    Returns Details about a ticket purchased by a specific user
    uid = > User's Id
    mid => Movie_Hall Id
    """
    movies = Ticket.objects.filter(user__id = uid, movie__id=mid)
    print(movies)
    purchase = Purchase.objects.filter(user__id = uid, movie__id=mid)
    seats=[]
    price = 0
    status = "Purchased"
    if len(purchase)>0:
        price = int((purchase.values()[0])["price"])
    else:
        movies1 = Ticket.objects.values("movie__hall__category__price", "discount__discount","status").filter(user__id = uid, movie__id=mid).first()
        price = int(movies1["movie__hall__category__price"])*len(movies) - int(movies1["discount__discount"])*len(movies)
        status = movies1["status"]
    for i in movies:
        seats.append(i.seats)
    
    context = {
        'movies':movies[0],
        'seats':seats,
        'activate_movies':"active"
    }
    if(len(purchase))>0:
        price *= len(purchase)
        status = "Purchased"
    context = {
    'movies':movies[0],
    'seats':seats,
    'purchase':status,
    'price':price,
    'activate_movies':"active",
    'uid':uid,
    'mid':mid
    }

    return render(request,'tickets/ticket_details.html',context)


def cancle_tickets(request,mid, uid):
    """Function to cancle user's seat bookings"""
    tic =  Ticket.objects.filter(user__id = uid, movie__id=mid)
    for i in tic:
        tick = Ticket.objects.get(id=i.id)
        tick.status = "Canceled"
        tick.save()
    return redirect('/accounts/dashboard/')

