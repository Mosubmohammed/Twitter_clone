from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from .forms import *

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        form=MeepForm(request.POST or None)
        if request.method=='POST':
            if form.is_valid():
                meep=form.save(commit=False)
                meep.user=request.user
                meep.save()
                messages.success(request,f"Your Meep Has Been Posted!")
                return redirect('home')
        meeps = Meep.objects.all().order_by('create_at')
        return render(request, 'home.html', {"meeps": meeps,"form": form})
    else:
        meeps = Meep.objects.all().order_by('create_at')
        return render(request, 'home.html', {"meeps":meeps})



def profile_list(request):
    if request.user.is_authenticated:
        profiles=Profile.objects.exclude(user=request.user)
        return render(request,'profile_list.html',{'profiles':profiles})
    else:
        messages.success(request,("you must be logged in"))
        return redirect('home')

def profile(request,pk):
    if request.user.is_authenticated:
        
        profile=Profile.objects.get(user_id=pk)
        meeps=Meep.objects.filter(user_id=pk)
        
        #post form logic
        if request.method=="POST":
            #get currunt user id
            current_user_profile=request.user.profile
            #get form data
            action=request.POST['follow']
            if action=="unfollow":
                current_user_profile.Follows.remove(profile)
            elif action=="follow":
                current_user_profile.Follows.add(profile)
            current_user_profile.save()
            

        return render(request, 'profile.html',{'profile':profile},{"meeps":meeps})
    else:
        messages.success(request,("you must be logged in"))
        return redirect('home')
    
def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("you have been logged in"))
            return redirect('home')
        else:
            messages.success(request,("invalid username or password"))
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout_user(request):
    logout(request)
    messages.success(request,("you have been logged out"))
    return redirect('home')