from django.urls import path
from .views import (
    
    QuizList,
    submit_quiz ,
    TopicListView,
    QuizDetailView,
    
)

app_name='quizes'

urlpatterns = [
    path('quizzes/', TopicListView.as_view(), name="topic-list"),
    path('quizzes/<str:topic>/', QuizList.as_view(), name="quiz-list-topic"),
    path('quizzes/<str:topic>/<int:pk>/', QuizDetailView.as_view(), name="quiz-detail"),
    path('quizzes/<str:topic>/<int:pk>/submit/', submit_quiz, name="submit_quiz"),

    
]
#quizes:main_view

