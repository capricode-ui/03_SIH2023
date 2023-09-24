from django.contrib import admin
from django.urls import path 

from quiz import views


urlpatterns = [
   path("quiz/",views.quiz,name='quiz')
]
urlpatterns = [
   path("login/",views.quiz,name='login')
]
