from django.db import models

topic_choices=(
    ('copyrights','Copyrights'),
    ('patents','Patents'),
    ('trademarks','Trademarks'),
)

# Create your models here.
class Quiz(models.Model):
    name=models.CharField(max_length=120)
    description=models.CharField(max_length=600)
    topic=models.CharField(max_length=60,choices=topic_choices)
    number_of_questions=models.IntegerField()
    required_score_to_pass=models.IntegerField(help_text="required score")
    
    def __str__(self):
        return f"{self.name}-{self.topic}"
    
    def get_questions(self):
        return  self.question_set.all()
    
    class Meta:
        verbose_name_plural='Quizes'
    
    
        
    
    

# Create your models here.
