from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html',{})