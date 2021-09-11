from django.shortcuts import render,redirect
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import User
from movies.models import Now_Showing, Up_Comming
from halls.models import  Category, Hall, Movie_Hall, Ticket
from django.contrib import messages
import json
from accounts.forms import ProfileForm,UserForm
from movies.forms import NowShowingForm, UpCommingForm
from halls.models import Purchase
from halls.forms import HallForm,CategoryForm, MovieHallForm
from tickets.models import Categories
from tickets.form import CategoriesForm, TicketForm
from accounts.models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from accounts.auth import admin_only

@admin_only
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

@admin_only
@login_required
def show_user(request):
    users = User.objects.all().filter(is_staff=0).order_by('-id')
    context={
        'user':users,
    }
    return render(request, 'admins/show_user.html',context)

@admin_only
@login_required
def show_admin(request):
    users = User.objects.all().filter(is_staff=1).order_by('-id')
    context={
        'user':users,
    }
    return render(request, 'admins/show_admin.html',context)

@admin_only
@login_required
def promote_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_staff=True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User promoted to admin')
    return redirect('/admins/show_user')

@admin_only
@login_required
def demote_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_staff=False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin Demoted to user')
    return redirect('/admins/show_user')

@admin_only
@login_required
def delete_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'User Deleted')
    return redirect('/admins/show_user')

@admin_only
@login_required
def delete_admin(request,user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'Admin Deleted')
    return redirect('/admins/show_admin')

@admin_only
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
    

@admin_only
@login_required
def deactivate(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Account Deactivated')
    return redirect('/admins/show_user')

@admin_only
@login_required
def activate(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Account Activated')
    return redirect('/admins/show_user')


@admin_only
@login_required
def show_movie(request):
    movies = Now_Showing.objects.all().order_by('-id')
    context={
        'movies':movies,
    }
    return render(request, 'admins/show_movies.html',context)

@admin_only
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

@admin_only
@login_required
def delete_movie(request,movie_id):
    movie = Now_Showing.objects.get(id=movie_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Movie Deleted')
    return redirect('/admins/show_movies')


@admin_only
@login_required
def up_movie(request):
    movies = Up_Comming.objects.all()
    context={
        'movies':movies,
    }
    return render(request, 'admins/up_movies.html',context)

@admin_only
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


@admin_only
@login_required
def delete_upmovie(request,movie_id):
    movie = Up_Comming.objects.get(id=movie_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Movie Deleted')
    return redirect('/admins/up_movies')




@admin_only
@login_required
def show_hall(request):
    hall = Hall.objects.all().order_by('-id')
    context={
        'hall':hall,
    }
    return render(request, 'admins/show_hall.html',context)


@admin_only   
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

@admin_only
@login_required
def delete_hall(request,hall_id):
    movie = Hall.objects.get(id=hall_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Hall Deleted')
    return redirect('/admins/show_hall')


@admin_only
@login_required
def hall_category(request):
    cat = Category.objects.all().order_by('-id')
    context={
        'cat':cat,
    }
    return render(request, 'admins/hall_category.html',context)

@admin_only   
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

@admin_only
@login_required
def delete_hall_cat(request,hallCat_id):
    movie = Category.objects.get(id=hallCat_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Hall Deleted')
    return redirect('/admins/hall_category')


@admin_only
@login_required
def movie_hall(request):
    mh = Movie_Hall.objects.all().order_by('-id')
    context={
        'cat':mh
    }
    return render(request, 'admins/movie_hall.html',context)

@admin_only   
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

@admin_only
@login_required
def delete_movie_hall(request,mh_id):
    mh = Movie_Hall.objects.get(id=mh_id)
    mh.delete()
    messages.add_message(request, messages.SUCCESS, 'Movie/Hall Deleted')
    return redirect('/admins/movie_hall')


@admin_only
@login_required
def show_ticket(request):
    tickets = Ticket.objects.all().order_by('-id')
    context={
        'ticket':tickets
    }
    return render(request, 'admins/show_ticket.html',context)


@admin_only    
@login_required
def purchase(request,tic_id):
    ticket = Ticket.objects.get(id=tic_id)
    ticket.status = "Purchased"
    ticket.save()
    messages.add_message(request, messages.SUCCESS, 'Ticket Marked as Purchased')
    return redirect('/admins/show_ticket')


@admin_only
@login_required
def reserve(request,tic_id):
    ticket = Ticket.objects.get(id=tic_id)
    ticket.status = "Booked"
    ticket.save()
    messages.add_message(request, messages.SUCCESS, 'Ticket Marked as Reserved')
    return redirect('/admins/show_ticket')


@admin_only
@login_required
def cancle(request,tic_id):
    ticket = Ticket.objects.get(id=tic_id)
    ticket.status = "Canceled"
    ticket.save()
    messages.add_message(request, messages.SUCCESS, 'Ticket Marked as Reserved')
    return redirect('/admins/show_ticket')

@admin_only
@login_required
def ticket_cat(request):
    ticket_cat = Categories.objects.all().order_by('-id')
    context={
        'tic':ticket_cat
    }
    return render(request, 'admins/ticket_category.html',context)

@admin_only    
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

@admin_only
@login_required
def delete_ticket_cat(request,tc_id):
    mh = Categories.objects.get(id=tc_id)
    mh.delete()
    messages.add_message(request, messages.SUCCESS, 'Ticket Category Deleted')
    return redirect('/admins/ticket_cat')

@admin_only
@login_required
def payments(request):
    purchase = Purchase.objects.all().order_by('-id')
    context={
        'purchases':purchase
    }
    return render(request, 'admins/show_payments.html',context)

@admin_only
@login_required
def create_User(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username, email = user.email, firstname = user.first_name, lastname = user.last_name)
            messages.add_message(request, messages.SUCCESS, "User Registered Successfully!")
            print("a")
            return redirect('/admins/show_user')

        else:
            messages.add_message(request, messages.ERROR,"User Registration Failed!")
            return render(request, 'admins/add_user.html', {'form':form})
        
    context={
        'form':form
    }
    return render(request, "admins/add_user.html", context)



@admin_only
@login_required
def create_Ticket(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ticket Booked Successfully!")
            return redirect('/admins/show_ticket')

        else:
            messages.add_message(request, messages.ERROR,"Ticket Booking Failed!")
            return render(request, 'admins/show_ticket.html', {'form':form})
        
    context={
        'form':form
    }
    return render(request, "admins/add_tickets.html", context)

@admin_only
@login_required
def create_Category(request):
    form = CategoriesForm()
    if request.method == "POST":
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Category Created Successfully!")
            return redirect('/admins/ticket_cat')

        else:
            messages.add_message(request, messages.ERROR,"Category Creation Failed!")
            return render(request, 'admins/ticket_cat.html', {'form':form})
        
    context={
        'form':form
    }
    return render(request, "admins/add_ticket_category.html", context)


@admin_only
@login_required
def add_hall(request):
    form = HallForm()
    if request.method == "POST":
        form = HallForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Category Created Successfully!")
            return redirect('/admins/show_hall')

        else:
            messages.add_message(request, messages.ERROR,"Category Creation Failed!")
            return render(request, 'admins/show_hall.html', {'form':form})
        
    context={
        'form':form
    }
    return render(request, "admins/add_hall.html", context)


@admin_only
@login_required
def add_hallCat(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Category Created Successfully!")
            return redirect('/admins/hall_category')

        else:
            messages.add_message(request, messages.ERROR,"Category Creation Failed!")
            return render(request, 'admins/hall_category.html', {'form':form})
        
    context={
        'form':form
    }
    return render(request, "admins/add_hall_cat.html", context)


@admin_only
@login_required
def add_nowShowing(request):
    form = NowShowingForm()
    if request.method == "POST":
        form = NowShowingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Movie Added  Successfully!")
            return redirect('/admins/show_movies')

        else:
            messages.add_message(request, messages.ERROR,"Movie Addition Failed!")
            return render(request, 'admins/add_now_showing.html', {'form':form})
        
    context={
        'form':form
    }
    return render(request, "admins/add_now_showing.html", context)


@admin_only
@login_required
def add_upComming(request):
    form = UpCommingForm()
    if request.method == "POST":
        form = UpCommingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Movie Added  Successfully!")
            return redirect('/admins/up_movies')

        else:
            messages.add_message(request, messages.ERROR,"Movie Addition Failed!")
            return render(request, 'admins/add_up_comming.html', {'form':form})
        
    context={
        'form':form
    }
    return render(request, "admins/add_up_comming.html", context)




@admin_only
@login_required
def admin_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.SUCCESS(request, "Account Updated Successfully")
            return redirect('admins/dashboard')
    context = {'form':form}
    return render (request, 'admins/profile.html', context)



@admin_only
@login_required
def update_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "User Details Updated Successfully")
            return redirect('/admins/profile/')
        else:
            messages.add_message(request, messages.ERROR,"User Update Failed!")
            return render(request, 'admins/update_profile.html', {'form':form})
        
    context={
        'form':ProfileForm(instance=profile)
    }
    return render(request, "admins/update_profile.html", context)


@admin_only
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/admins/profile')
        else:
            messages.add_message(request, messages.ERROR,"Something Went Wrong!")
            return render(request, 'admins/change_password.html', {'form':form})

    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form':form}
        return render(request, 'admins/change_password.html', context)