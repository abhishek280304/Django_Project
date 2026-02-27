from django.urls import path
from .views import *

urlpatterns=[
    path('',register_,name='register_'),
    path('login_./',login_,name='login_'),
    path('logout_',logout_,name='logout_'),
    path('profile/',profile,name='profile'),
    path('reset_pass/',reset_pass,name='reset_pass'),
    path('forget_pass/',forget_pass,name='forget_pass'),
    path('new_password/',new_password,name='new_password')
]