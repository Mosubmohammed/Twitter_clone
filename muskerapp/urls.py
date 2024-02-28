from django.urls import path
from .views import *



urlpatterns = [
    path('',home,name="home"),
    path('profile_list/',profile_list,name="profile_list"),
    path('profile/<int:pk>',profile,name="profile"),
    path('profile/followers/<int:pk>',followers,name="followers"),
        path('profile/follows/<int:pk>',follows,name="follows"),
    path('login/',login_user, name='login'),
    path('logout',logout_user, name='logout'),
    path('register ',register_user, name='register'),
    path('update_user ',update_user, name='update_user'),
    path('meep_like/<int:pk>',meep_like, name='meep_like'),
    path('meep_show/<int:pk>',meep_show, name='meep_show'),
    path('unfollow/<int:pk>',unfollow, name='unfollow'),
    path('follow/<int:pk>',follow, name='follow'),
        path('delete_meep/<int:pk>',delete_meep, name='delete_meep'),
        path('edit_meep/<int:pk>',edit_meep, name='edit_meep'),
         path('search',search, name='search'),

    
]
