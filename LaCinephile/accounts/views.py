from .models import Profile
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from .forms import ProfileForm, UserForm
from django.contrib import messages
from .forms import LoginForm
from .auth import unauthenticated_user, user_only
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@unauthenticated_user
def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username, email = user.email, firstname = user.first_name, lastname = user.last_name)
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
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('/admins/dashboard')
                elif not user.is_staff:
                    login(request, user)
                    return redirect('/')
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

@user_only
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

@user_only
@login_required
def update_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "User Details Updated Successfully")
            return redirect('/accounts/profile')
        else:
            messages.add_message(request, messages.ERROR,"User Update Failed!")
            return render(request, 'accounts/update_profile.html', {'form':form})
        
    context={
        'form':ProfileForm(instance=profile)
    }
    return render(request, "accounts/update_profile.html", context)

@user_only
@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            messages.add_message(request, messages.ERROR,"Something Went Wrong!")
            return render(request, 'accounts/profile.html', {'form':form})

    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form':form}
        return render(request, 'accounts/change_password.html', context)






