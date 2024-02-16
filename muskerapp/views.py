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

def profile(request,pk):
    if request.user.is_authenticated:
        
        profile=Profile.objects.get(user_id=pk)
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
            

        return render(request, 'profile.html',{'profile':profile})
    else:
        messages.success(request,("you must be logged in"))
        return redirect('home')