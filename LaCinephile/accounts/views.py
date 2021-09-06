from django.contrib.auth.models import User
from .models import Profile, Profile
from django.contrib.auth import forms, logout, login, authenticate
from django.shortcuts import redirect, render
from .forms import ProfileForm, UserForm
from django.contrib import messages
from .forms import LoginForm
from .auth import unauthenticated_user, user_only
from django.contrib.auth.decorators import  login_required


@unauthenticated_user
def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(User=user, username=user.username)
            messages.add_message(request, messages.SUCCESS, "User Registered Successfully. Please Login to continue")
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,"User Registration Failed!")
            return render(request, 'accounts/register.html', {'form':form})
        
    context={
        'form':form
    }
    return render(request, "accounts/register.html", context)

@unauthenticated_user
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            print(user)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('/accounts/register')
                elif not user.is_staff:
                    login(request, user)
                    return redirect('/accounts/dashboard/{{user.id}}')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid Username or Password')
                return render(request, 'accounts/login.html', {'form_login':form})
    context = {
        'form_login': LoginForm
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/accounts/login')


@login_required

def user_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.SUCCESS(request, "Account Updated Successfully")
            return redirect('/profile')
    context = {'form':form}
    return render (request, 'accounts/profile.html', context)





