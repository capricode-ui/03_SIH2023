from django.contrib import admin
from django.urls import path 

from quiz import views


urlpatterns = [

   # path("login/",views.quiz,name='login'),
   path("quiz/",views.quiz,name='quiz'),
   
]

