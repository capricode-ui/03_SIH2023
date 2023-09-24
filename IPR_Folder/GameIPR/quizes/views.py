from django.shortcuts import render,get_object_or_404,redirect
from .models import Quiz
from django.views.generic import ListView,DetailView
from .models import topic_choices
from questions.models import Question

class TopicListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'
    context_object_name = 'topics'

    def get_queryset(self):
        return topic_choices



class QuizList(ListView):
    model=Quiz
    template_name='quizes/quizlist.html'
    context_object_name = 'quizzes' 
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.kwargs.get('topic', None)
        context['topic'] = topic  # Pass 'topic' to the template
        return context
    
    
    def get_queryset(self):
        topic = self.kwargs.get('topic', None)
        if topic:
            return Quiz.objects.filter(topic=topic)
        else:
            return Quiz.objects.all()
    
    
    


class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quizes/quiz_detail.html'
    context_object_name = 'quiz'
    



def submit_quiz(request, topic, pk):
    try:
        quiz = Quiz.objects.get(topic=topic, pk=pk)
        questions = Question.objects.filter(quiz=quiz)
    except (Quiz.DoesNotExist, Question.DoesNotExist):
        return redirect('topic-list')  # Redirect to the topic list if quiz or questions not found

    if request.method == 'POST':
        score = 0
        incorrectly_answered = []

        for question in questions:
            user_answer_key = f'question_{question.id}'
            correct_option = question.correct_option
            user_answer = request.POST.get(user_answer_key, '').strip().upper()  # Get user's answer and convert to uppercase

            if user_answer == correct_option:
                score += 1
                
            else:
                incorrectly_answered.append(question)

        total_questions = len(questions)
        percentage_score = (score / total_questions) * 100

        return render(request, 'quizes/quiz_results.html', {'score': score, 'percentage_score': percentage_score ,'quiz':quiz,'incorrect':incorrectly_answered,'total_questions':total_questions})

    return redirect('quiz-detail', topic=topic, pk=pk)  # Redirect to the quiz detail page if not a POST request


    
    


# Create your views here.
