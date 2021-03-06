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
from django.core.paginator import EmptyPage, Paginator


@admin_only
@login_required
def dashboard(request):
    """Function for retriving admin dashboard"""
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count() #User count
    admin_count = users.filter(is_staff=1).count()# Admin Count
    movies_count = Now_Showing.objects.all().count()# All movie count

    ticket = Ticket.objects.all()
    ticket_count = ticket.count()# Akk ticket count

    tickets = Ticket.objects.all()
    data=[0,0,0] #Empty initialized data array

    canceled = ticket.filter(status="Canceled")
    canc_data = [0,0,0] #Empty initialized data array
    for i in canceled: # Categorize ticket data for displaying in admin panal
        if i.movie.hall.category.name == "GOLD":
            canc_data[0] += 1
        elif i.movie.hall.category.name == "PLATINUM":
            canc_data[1] +=1
        else:
            canc_data[2]+=1

    for i in tickets: # Categorize hall data for displaying in admin panal
        if i.movie.hall.category.name == "GOLD":
            data[0] += 1
        elif i.movie.hall.category.name == "PLATINUM":
            data[1] +=1
        else:
            data[2]+=1

    ticket = ticket.order_by('-id')[:5] # Retrieve 5 recent tickets
    context={
        'user_count':user_count,
        'admin_count':admin_count,
        'movies_count':movies_count,
        'tickets_count':ticket_count,
        'data':json.dumps(data),
        'canc_data': json.dumps(canc_data),
        'ticket':ticket,
        'activate_home':'active'
    }
   

    return render(request, 'admins/dashboard.html',context)

@admin_only
@login_required
def show_user(request):
    """Function to show all users in admin page"""
    if 'q' in request.GET:
        q=request.GET['q']
        users = User.objects.filter(first_name__icontains=q).filter(is_staff=0)
    else:
        users = User.objects.all().filter(is_staff=0).order_by('-id')
    context={
        'user':users,
        'activate_user':'active'
    }
    return render(request, 'admins/show_user.html',context)

@admin_only
@login_required
def show_admin(request):
    """Function to view all admins/staff in admin page"""
    if 'q' in request.GET:
        q=request.GET['q']
        users = User.objects.filter(first_name__icontains=q).filter(is_staff=1)
    else:
        users = User.objects.all().filter(is_staff=1).order_by('-id')
    context={
        'user':users,
        'activate_admin':'active'
    }
    return render(request, 'admins/show_admin.html',context)

@admin_only
@login_required
def promote_user(request,user_id):
    """Function to promote users"""
    user = User.objects.get(id=user_id)
    user.is_staff=True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User promoted to admin')
    return redirect('/admins/show_user')

@admin_only
@login_required
def demote_user(request,user_id):
    """Function to demote users"""
    user = User.objects.get(id=user_id)
    user.is_staff=False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin Demoted to user')
    return redirect('/admins/show_user')

@admin_only
@login_required
def delete_user(request,user_id):
    """Function to delete users"""
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'User Deleted')
    return redirect('/admins/show_user')

@admin_only
@login_required
def delete_admin(request,user_id):
    """Function to delete admin"""
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'Admin Deleted')
    return redirect('/admins/show_admin')

@admin_only
@login_required
def update_user(request,user_id):
    """Function to update users"""
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
    """Function to deactivate users"""
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Account Deactivated')
    return redirect('/admins/show_user')

@admin_only
@login_required
def activate(request,user_id):
    """Function to activate users"""
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Account Activated')
    return redirect('/admins/show_user')


@admin_only
@login_required
def show_movie(request):
    """Function to display all movies from database for admin to view"""
    if 'q' in request.GET:
        q=request.GET['q']
        movies = Now_Showing.objects.filter(name__icontains=q)
    else:
        movies = Now_Showing.objects.all().order_by('-id')
    context={
        'movies':movies,
        'activate_now':'active'
    }
    return render(request, 'admins/show_movies.html',context)

@admin_only
@login_required
def update_movie(request,movie_id):
    """Function to update movie details"""
    movie = Now_Showing.objects.get(id=movie_id)
    form = NowShowingForm(instance=movie)
    if request.method == "POST":
        form = NowShowingForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Movie Updated Successfully")
            return redirect('/admins/show_movies')
    context = {'form':form,'activate_now':'active'}
    return render (request, 'admins/edit_movie.html', context)

@admin_only
@login_required
def delete_movie(request,movie_id):
    """Function to delete movies"""
    movie = Now_Showing.objects.get(id=movie_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Movie Deleted')
    return redirect('/admins/show_movies')


@admin_only
@login_required
def up_movie(request):
    """Function to show up-comming movies"""
    if 'q' in request.GET:
        q=request.GET['q']
        movies = Up_Comming.objects.filter(name__icontains=q)
    else:
        movies = Up_Comming.objects.all()
    context={
        'movies':movies,
        'activate_up':'active'
    }
    return render(request, 'admins/up_movies.html',context)

@admin_only
@login_required
def update_upmovie(request,movie_id):
    """Function to update upcomming movies"""
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
    """Function to show halls"""
    hall = Hall.objects.all().order_by('-id')
    context={
        'hall':hall,
        'activate_hall':'active'
    }
    return render(request, 'admins/show_hall.html',context)


@admin_only   
@login_required
def update_hall(request,hall_id):
    """Function to update halls"""
    hall = Hall.objects.get(id=hall_id)
    form = HallForm(instance=hall)
    if request.method == "POST":
        form = HallForm(request.POST, instance=hall)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Hall Details Updated Successfully")
            return redirect('/admins/show_hall')

    context = {'form':form,'activate_hall':'active'}
    return render (request, 'admins/edit_hall.html', context)

@admin_only
@login_required
def delete_hall(request,hall_id):
    """Function to delete halls"""
    movie = Hall.objects.get(id=hall_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Hall Deleted')
    return redirect('/admins/show_hall')


@admin_only
@login_required
def hall_category(request):
    """Function to show hall categories"""
    cat = Category.objects.all().order_by('-id')
    context={
        'cat':cat,
        'activate_hall_cat':'active'
    }
    return render(request, 'admins/hall_category.html',context)

@admin_only   
@login_required
def update_hall_cat(request,hallCat_id):
    """Function to update hall category"""
    hall = Category.objects.get(id=hallCat_id)
    form = CategoryForm(instance=hall)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=hall)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Category Details Updated Successfully")
            return redirect('/admins/hall_category')

    context = {'form':form,'activate_hall_cat':'active'}
    return render (request, 'admins/edit_hallCategory.html', context)

@admin_only
@login_required
def delete_hall_cat(request,hallCat_id):
    """Function to delete hall category"""
    movie = Category.objects.get(id=hallCat_id)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, 'Hall Deleted')
    return redirect('/admins/hall_category')


@admin_only
@login_required
def movie_hall(request):
    """Function to show movie halls"""
    mh = Movie_Hall.objects.all().order_by('-id')
    context={
        'cat':mh,
        'activate_hall_all':'active'
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

    context = {'form':form,'activate_hall_all':'active'}
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
    if 'q' in request.GET:
        q=request.GET['q']
        tickets = Ticket.objects.filter(user__first_name__icontains=q)
    else:
        tickets = Ticket.objects.all().order_by('-id')
    p= Paginator(tickets,10)
    page_num = request.GET.get("page",1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    
    context={
        'ticket':page,
        'activate_ticket':'active',
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
    messages.add_message(request, messages.SUCCESS, 'Ticket Marked as Cancelled')
    return redirect('/admins/show_ticket')

@admin_only
@login_required
def ticket_cat(request):
    ticket_cat = Categories.objects.all().order_by('-id')
    context={
        'tic':ticket_cat,
        'activate_ticket_cat':'active',
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

    context = {'form':form,'activate_ticket_cat':'active'}
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
    if 'q' in request.GET:
        q=request.GET['q']
        purchase = Purchase.objects.filter(user__first_name__icontains=q)
    else:
        purchase = Purchase.objects.all().order_by('-id')
    p= Paginator(purchase,10)
    page_num = request.GET.get("page",1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context={
        'purchases':page,
        'activate_purchase':'active',
    }
    return render(request, 'admins/show_payments.html',context)


@admin_only
@login_required
def create_User(request):
    """Function to create users"""
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
    """Function to create tickets"""
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
def add_movie_hall(request):
    form = MovieHallForm()
    if request.method == "POST":
        form = MovieHallForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Show time added Successfully!")
            return redirect('/admins/movie_hall')

        else:
            messages.add_message(request, messages.ERROR,"Failed to add show time!")
            return render(request, 'admins/movie_hall.html', {'form':form})
        
    context={
        'form':form
    }
    return render(request, "admins/add_movie_hall.html", context)


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
    context = {'form':form, "activate_home":"active"}
    return render (request, 'admins/profile.html', context)



@admin_only
@login_required
def update_profile(request):
    """Function to update user profiles"""
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
    """Function to change password"""
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
