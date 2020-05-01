from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomRegistorForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = CustomRegistorForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New user Created, Login to get started"))
            return redirect ('auth')
        

    else:
        register_form = CustomRegistorForm()
    return render(request, 'register.html', {'register_form': register_form})

