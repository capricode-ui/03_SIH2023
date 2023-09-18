from django.shortcuts import render, redirect
from .models import QuizQuestion

def quiz(request):
    
    # Get all quiz questions from the database
    questions = QuizQuestion.objects.all()
    

    # Get the current question index from the session or initialize it to 0
    current_question_index = request.session.get('current_question_index', 0)

    # Get the current question based on the index
    current_question = questions[current_question_index] if current_question_index < len(questions) else None

    # Initialize variables to store user's answer and correctness
    user_answer = None
    is_correct = None

    if request.method == 'POST':
        # If the form is submitted, get the user's selected answer
        user_answer = request.POST.get('user_answer', '').upper()  # Assuming answer is stored as 'A', 'B', 'C', 'D'

        # Check if the user's answer is correct
        correct_answer = current_question.correct_option
        is_correct = user_answer == correct_answer
        
        

        # Increment the current question index to move to the next question
        current_question_index += 1
        
        

    # Update the session with the new current question index
    request.session['current_question_index'] = current_question_index
    
    if current_question_index >= len(questions):
           request.session.clear()  
    
    
    
    

    context = {
        'current_question': current_question,  # The question to display
        'user_answer': user_answer,            # The user's selected answer
        'is_correct': is_correct,              # Whether the answer is correct or not
    }
    return render(request, 'quiz.html', context)
