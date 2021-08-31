import re
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib import messages

# Create your views here.

def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print("Valid")
            form.save()
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,"User Registration Failed!")
            return render(request, 'accounts/register.html', {'form':form})
        
    context={
        'form':form
    }
    return render(request, "accounts/register.html", context)