from django.contrib import admin
from django.urls import path 

# from home import views

from django.contrib.auth import views as auth_views
from .views import index,login, signup, logout_user

urlpatterns = [
   # path("",views.index,name='home'),
   # path("login",views.login,name='login'),
   # path("signup",views.signup,name='signup'),

   path("",index,name='index'),
   path("login",login,name='login'),
   path("signup",signup,name='signup'),
   

   # path("register", register, name="register"),
   # path("login_user", login_user, name="login_user"),
   path("logout_user", logout_user, name="logout_user"),
   
   
 
]
