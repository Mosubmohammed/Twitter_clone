from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html',{})


def profile_list(request):
    if request.user.is_authenticated:
        profiles=Profile.objects.exclude(user=request.user)
        return render(request,'profile_list.html',{'profiles':profiles})
    else:
        messages.success(request,("you must be logged in"))
        return redirect('home')
    