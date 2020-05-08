from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime,timedelta

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text  
    
    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.answer_text

