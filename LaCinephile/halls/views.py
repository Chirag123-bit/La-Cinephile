from django.shortcuts import redirect, render
from .models import Category, Purchase
from tickets.models import Categories as ticket
from movies.models import Now_Showing 
from halls.models import Ticket
from django.http import JsonResponse
from django.views.generic import View
from halls.models import Movie_Hall
import datetime
from tickets.models import Categories
from django.urls import reverse
from django.contrib import messages

from accounts.auth import unauthenticated_user, user_only
from django.contrib.auth.decorators import  login_required
import requests

@user_only
def prices(request):
    hall_cat = Category.objects.all()
    ticket_cat = ticket.objects.all()
    context={
        'activate_prices':'active',
        'hall_cat':hall_cat,
        'ticket_cat':ticket_cat
    }
    return render(request, 'halls/price.html',context)

@login_required
def book(request):
    """Function for booking/purchasing a movie"""
    mh = Movie_Hall.objects.all()
    if request.method == "POST":
        data = request.POST
        user = request.user
        movie = data.get('mid')
        seats = data.get('seat_selected')
        discount = data.get('discountId')
        print(user.id)
         

        mv = Movie_Hall.objects.filter(id=int(movie))[0] #Gets corresponding movie-time
        dis = Categories.objects.filter(id=int(discount))[0] #Gets hall category for discount

        count = round(len(seats)/3) #Gets total numbers of seats selected by user
        #accounts for commas(,) length of seat(Eg: A1, B1)::: hence no.of seats is given by length/3 

        total = (count*int(data.get('inprice')))
        ticket = Ticket(user=user, movie=mv, seats=seats, discount=dis)
        if "book" in request.POST: #For Booking
            status = "Booked"
            i=0
            while(i<len(seats)):
                ticket = Ticket(user=user, movie=mv, seats=seats[i:i+2], discount=dis, status=status)
                i+=3
                ticket.save()
            messages.add_message(request, messages.SUCCESS, "Tickets Booked SuccessFully")
            return redirect("/tickets/detail/"+str(user.id)+"/"+str(movie))
        else: #For Purchasing
            status = 'Purchased'
            i=0
            while(i<len(seats)):
                ticket = Ticket(user=user, movie=mv, seats=seats[i:i+2], discount=dis, status=status)
                ticket.save()
                i+=3
            purchase = Purchase(user=user, movie=mv, seats=seats, discount=dis, price = total, status=status)
            purchase.save()

            return redirect(reverse('halls:khaltirequest')+"?o_id="+str(purchase.id))

    context={
        'activate_book':'active',
        'mh':mh
    }
    return render(request, 'halls/reservation.html',context)




@user_only
def movie_json(request):
    movies = list(Now_Showing.objects.values())
    return JsonResponse({'data':movies})


@user_only
def hall_json(request, *args, **kwargs):
    """Function for returning JSON data of hall based on selected movie"""
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


@user_only
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


@user_only
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

@user_only
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



@user_only
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





class KhaltiRequestView(View):
    def get(self, request, *args, **kwargs):
        id = int(request.GET.get("o_id"))
        detail = Purchase.objects.get(id=id)

        context={
            "order":detail
        }

        return render(request, 'tickets/khaltirequest.html', context)


class KhaltiVerifyView(View):
    """Class-based function for verifying Payment"""
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        amount = request.GET.get("amount")
        o_id = int(request.GET.get("order_id"))

        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
        "token": token,
        "amount": amount
        }
        headers = {
        "Authorization": "KEY test_secret_key_251242f46ea74d79b6e1fb3f4fd86bef"
        }

        order_obj = Purchase.objects.get(id=o_id)

        response = requests.post(url, payload, headers = headers)
        resp_dict = response.json()
        if resp_dict.get("idx"):
            success = True
            order_obj.payment_completed = True
            order_obj.status = "Purchased"
            order_obj.save()
    
        else:
            success = False
        
        print(order_obj)

        data = {
            "success":success
        }
        return JsonResponse(data)