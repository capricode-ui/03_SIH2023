from django.urls import path
from .views import (
    
    
    TopicListView,
    
    
)

app_name='quizes'

urlpatterns = [
    path('quizzes/', TopicListView.as_view(), name="topic-list"),
    
]