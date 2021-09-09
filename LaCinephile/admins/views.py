from django.shortcuts import render,redirect
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import User
from movies.models import Now_Showing, Up_Comming
from halls.models import  Category, Hall, Movie_Hall, Ticket
from django.contrib import messages
import json
from accounts.forms import ProfileForm
from movies.forms import NowShowingForm, UpCommingForm
from halls.models import Purchase
from halls.forms import HallForm,CategoryForm, MovieHallForm
from tickets.models import Categories
from tickets.form import CategoriesForm


@login_required
def dashboard(request):
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    movies_count = Now_Showing.objects.all().count()

    ticket = Ticket.objects.all()
    ticket_count = ticket.count()

    tickets = Ticket.objects.all()
    data=[0,0,0]

    canceled = ticket.filter(status="Canceled")
    canc_data = [0,0,0]
    for i in canceled:
        if i.movie.hall.category.name == "GOLD":
            canc_data[0] += 1
        elif i.movie.hall.category.name == "PLATINUM":
            canc_data[1] +=1
        else:
            canc_data[2]+=1

    print(canc_data)

    for i in tickets:
        if i.movie.hall.category.name == "GOLD":
            data[0] += 1
        elif i.movie.hall.category.name == "PLATINUM":
            data[1] +=1
        else:
            data[2]+=1

    ticket = ticket.order_by('-id')[:5] 
    print(ticket)
    context={
        'user_count':user_count,
        'admin_count':admin_count,
        'movies_count':movies_count,
        'tickets_count':ticket_count,
        'data':json.dumps(data),
        'canc_data': json.dumps(canc_data),
        'ticket':ticket,
    }
   

    return render(request, 'admins/dashboard.html',context)

@login_required
def show_user(request):
    users = User.objects.all().filter(is_staff=0).order_by('-id')
    context={
        'user':users,
    }
    return render(request, 'admins/show_user.html',context)

@login_required
def promote_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_staff=True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User promoted to admin')
    return redirect('/admins/show_user')

@login_required
def delete_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'User Deleted')
    return redirect('/admins/show_user')

@login_required
def update_user(request,user_id):
    user = User.objects.get(id=user_id)
    profile = user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Account Updated Successfully")
            return redirect('/admins/show_user')
    context = {'form':form}
    return render (request, 'admins/edit_user.html', context)
    

@login_required
def deactivate(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Account Deactivated')
    return redirect('/admins/show_user')

@login_required
def activate(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Account Activated')
    return redirect('/admins/show_user')


@login_required
def show_movie(request):
    movies = Now_Showing.objects.all().order_by('-id')
    context={
        'movies':movies,
    }
    return render(request, 'admins/show_movies.html',context)

@login_required
def update_movie(request,movie_id):
    movie = Now_Showing.objects.get(id=movie_id)
    form = NowShowingForm(instance=movie)
    if request.method == "POST":
        form = NowShowingForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Movie Updated Successfully")
            return redirect('/admins/show_movies')
    context = {'form':form}
    return render (request, 'admins/edit_movie.html', context)

@login_required
def delete_movie(request,movie_id):
    movie = Now_Showing.objects.get(id=movie_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Movie Deleted')
    return redirect('/admins/show_movies')


@login_required
def up_movie(request):
    movies = Up_Comming.objects.all()
    context={
        'movies':movies,
    }
    return render(request, 'admins/up_movies.html',context)

@login_required
def update_upmovie(request,movie_id):
    movie = Up_Comming.objects.get(id=movie_id)
    form = UpCommingForm(instance=movie)
    if request.method == "POST":
        form = UpCommingForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Movie Updated Successfully")
            return redirect('/admins/up_movies')
    context = {'form':form}
    return render (request, 'admins/edit_upmovie.html', context)


@login_required
def delete_upmovie(request,movie_id):
    movie = Up_Comming.objects.get(id=movie_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Movie Deleted')
    return redirect('/admins/up_movies')





@login_required
def show_hall(request):
    hall = Hall.objects.all().order_by('-id')
    context={
        'hall':hall,
    }
    return render(request, 'admins/show_hall.html',context)

    
@login_required
def update_hall(request,hall_id):
    hall = Hall.objects.get(id=hall_id)
    form = HallForm(instance=hall)
    if request.method == "POST":
        form = HallForm(request.POST, instance=hall)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Hall Details Updated Successfully")
            return redirect('/admins/show_hall')

    context = {'form':form}
    return render (request, 'admins/edit_hall.html', context)

@login_required
def delete_hall(request,movie_id):
    movie = Hall.objects.get(id=movie_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Hall Deleted')
    return redirect('/admins/show_hall')



@login_required
def hall_category(request):
    cat = Category.objects.all().order_by('-id')
    context={
        'cat':cat,
    }
    return render(request, 'admins/hall_category.html',context)

    
@login_required
def update_hall_cat(request,hallCat_id):
    hall = Category.objects.get(id=hallCat_id)
    form = CategoryForm(instance=hall)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=hall)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Category Details Updated Successfully")
            return redirect('/admins/hall_category')

    context = {'form':form}
    return render (request, 'admins/edit_hallCategory.html', context)

@login_required
def delete_hall_cat(request,hallCat_id):
    movie = Category.objects.get(id=hallCat_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Hall Deleted')
    return redirect('/admins/hall_category')



@login_required
def movie_hall(request):
    mh = Movie_Hall.objects.all().order_by('-id')
    context={
        'cat':mh
    }
    return render(request, 'admins/movie_hall.html',context)

    
@login_required
def update_movie_hall(request,mh_id):
    mh = Movie_Hall.objects.get(id=mh_id)
    form = MovieHallForm(instance=mh)
    if request.method == "POST":
        form = MovieHallForm(request.POST, instance=mh)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Movie/Hall Details Updated Successfully")
            return redirect('/admins/movie_hall')

    context = {'form':form}
    return render (request, 'admins/edit_moviehall.html', context)

@login_required
def delete_movie_hall(request,mh_id):
    mh = Movie_Hall.objects.get(id=mh_id)
    mh.delete()
    messages.add_message(request, messages.SUCCESS, 'Movie/Hall Deleted')
    return redirect('/admins/movie_hall')


@login_required
def show_ticket(request):
    tickets = Ticket.objects.all().order_by('-id')
    context={
        'ticket':tickets
    }
    return render(request, 'admins/show_ticket.html',context)

    
@login_required
def purchase(request,tic_id):
    ticket = Ticket.objects.get(id=tic_id)
    ticket.status = "Purchased"
    ticket.save()
    messages.add_message(request, messages.SUCCESS, 'Ticket Marked as Purchased')
    return redirect('/admins/show_ticket')

@login_required
def reserve(request,tic_id):
    ticket = Ticket.objects.get(id=tic_id)
    ticket.status = "Booked"
    ticket.save()
    messages.add_message(request, messages.SUCCESS, 'Ticket Marked as Reserved')
    return redirect('/admins/show_ticket')

@login_required
def cancle(request,tic_id):
    ticket = Ticket.objects.get(id=tic_id)
    ticket.status = "Canceled"
    ticket.save()
    messages.add_message(request, messages.SUCCESS, 'Ticket Marked as Reserved')
    return redirect('/admins/show_ticket')


@login_required
def ticket_cat(request):
    ticket_cat = Categories.objects.all().order_by('-id')
    context={
        'tic':ticket_cat
    }
    return render(request, 'admins/ticket_category.html',context)

    
@login_required
def update_ticket_cat(request,tc_id):
    mh = Categories.objects.get(id=tc_id)
    form = CategoriesForm(instance=mh)
    if request.method == "POST":
        form = CategoriesForm(request.POST, instance=mh)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Category Details Updated Successfully")
            return redirect('/admins/ticket_cat')

    context = {'form':form}
    return render (request, 'admins/edit_ticket_cat.html', context)

@login_required
def delete_ticket_cat(request,tc_id):
    mh = Categories.objects.get(id=tc_id)
    mh.delete()
    messages.add_message(request, messages.SUCCESS, 'Ticket Category Deleted')
    return redirect('/admins/ticket_cat')

@login_required
def payments(request):
    purchase = Purchase.objects.all().order_by('-id')
    context={
        'purchases':purchase
    }
    return render(request, 'admins/show_payments.html',context)