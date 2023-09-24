from django.db import models
from quizes.models import Quiz


class Question(models.Model):
    quiz = models.ForeignKey('quizes.Quiz', on_delete=models.CASCADE)
    text=models.CharField(max_length=500)
    image_url= models.URLField(null=True,blank=True)
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    correct_option = models.CharField(max_length=100, help_text="Enter the correct option (e.g., 'A', 'B', 'C', or 'D')")
    solution=models.CharField(max_length=500)
    
    
    
    
    def __str__(self):
        return str(self.text)
    
    
    
    
    

 
# Create your models here.
