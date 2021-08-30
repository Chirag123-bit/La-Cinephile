from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

# Create your views here.

def register(request):
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    context={
        'form':form
    }
    return render(request, "accounts/register.html", context)