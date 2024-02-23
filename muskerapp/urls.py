from django.urls import path
from .views import *



urlpatterns = [
    path('',home,name="home"),
     path('profile_list/',profile_list,name="profile_list"),
    path('profile/<int:pk>',profile,name="profile"),
    path('login/',login_user, name='login'),
    path('logout',logout_user, name='logout'),
    path('register ',register_user, name='register'),
    path('update_user ',update_user, name='update_user'),
    path('meep_like/<int:pk>',meep_like, name='meep_like'),
    path('meep_show/<int:pk>',meep_show, name='meep_show'),
]
