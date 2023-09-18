from django.contrib import admin
from django.urls import path 

from quiz import views


urlpatterns = [
   path("",views.quiz,name='quiz')
 
]
