from django.contrib import admin
from django.urls import path 

# from home import views

from django.contrib.auth import views as auth_views
from .views import index,login, signup, logout_user,copyindex

urlpatterns = [
   path("",index,name='index'),
   path("copyindex",copyindex,name='copyindex'),
   path("login",login,name='login'),
   path("signup",signup,name='signup'),
   path("logout_user", logout_user, name="logout_user"),
]
