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
    movies = Now_Showing.objects.all()
    mh = Movie_Hall.objects.all()
    context={
        'activate_book':'active',
        'mh':mh
    }
    return render(request, 'halls/reservation.html',context)




