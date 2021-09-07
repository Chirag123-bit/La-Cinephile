from django.shortcuts import render
from halls.models import Ticket

def detail(request, uid, mid):
    movies = Ticket.objects.filter(user__id = uid, movie__id=mid)
    
    seats=[]
    for i in movies:
        seats.append(i.seats)
    
    context = {
        'movies':movies[0],
        'seats':seats,
        'activate_movies':"active"
    }

    return render(request,'tickets/ticket_details.html',context)