from django.db import models

class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=700)
    question_image=models.ImageField(null=True ,blank=True )
    image_url = models.URLField(null=True,blank=True)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100, help_text="Enter the correct option (e.g., 'A', 'B', 'C', or 'D')")
    solution_text=models.CharField(max_length=1000, null=True , blank=True)

    def __str__(self):
        return self.question_text
