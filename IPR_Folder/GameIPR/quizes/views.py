from django.shortcuts import render 
from .models import Quiz
from django.views.generic import ListView
from .models import topic_choices

class TopicListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'
    context_object_name = 'topics'

    def get_queryset(self):
        return topic_choices
    
    
    

# Create your views here.
